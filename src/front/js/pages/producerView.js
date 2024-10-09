import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import { Link, useNavigate, Navigate, useParams } from "react-router-dom";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import { Product } from "./ViewProducts";

export const ProducerView = () => {

    const { actions, store } = useContext(Context);
    const { producerId } = useParams();
    const navigate = useNavigate();
    const [ cautionDeleting, setCautionDeleting ] = useState(false);
    const autenticate = store.isLogedIn;
    const [ isLoading, setIsLoading ] = useState(true)
    
    useEffect(() => {
        actions.checkToken().then(() => {
            setIsLoading(false)
            
        });
        actions.getCategorieImg();
        actions.getProducer(producerId);
        actions.getProducts();
        actions.getCategories();
    }, [producerId]);
    if (isLoading) {
        // Muestra un mensaje o un spinner de carga mientras se verifica la autenticación
        return <div>Cargando...</div>;
    }

    if (!autenticate){
        return <Navigate to="/producer/login" />
    }
    
    const handleCautionDelete = () => {
        setCautionDeleting(true) 
    }
    const handleGoToAddProduct = () => {
        navigate(`/producer/dashboard/${producerId}/newproduct`)
    }
    
    const handleDelete = () => {
        actions.deleteProduct(id)
        
    }
    const handleEdit = () => {
        console.log("go to edit product view");
        
    }

    return (
        <>
        <h1 className="my-3">This is the producer view</h1>
        {/* <div>
            <img src={imageUrls[currentIndex]} alt="Descripción de la imagen" style={{ maxWidth: '100%', height: 'auto' }} />
            <button onClick={changeImage}>Cambiar Imagen</button>
        </div> */}
        {store.producers.map((producer, index) => 
        <div key={index}>
            <h3>Nombre de la compañía: {producer.brand_name || "no brand_name"}</h3>
            <h1>Hola, {producer.user_name || "no username"} {producer.user_last_name || "no user_last_name"}!</h1>
            <Link to={"/producer/form/" + producer.id}>
                <button type="button" className="edit btn btn-warning">Edita tu información o de la empresa aquí</button>
            </Link>

            {store.products.length > 0 ? (
                <Product />
            ) : (
                <button className="btn btn-primary" onClick={()=>handleGoToAddProduct()}>Añade nuevos productos</button>
            )}
            </div>

        )} 
        
        </>

    )
};
