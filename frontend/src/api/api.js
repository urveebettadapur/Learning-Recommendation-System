import axios from "axios";


const API = axios.create({

    baseURL: "http://127.0.0.1:8000"

});


export const generateLearningPath = async (data) => {

    const response = await API.post(
        "/recommend-learning-path",
        data
    );

    return response.data;

};