package com.crudweb.service;

import com.crudweb.model.Carro;
import com.crudweb.repository.CarroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.NoSuchElementException;

@Service
public class CarroService {

    @Autowired()
    private CarroRepository repository;

    public Carro saveCarro(Carro carro){
        try {
            return repository.save(carro);
        } catch (IllegalArgumentException illegal){
            return null;
        }
    }

    public List<Carro> findAllCarro(){
        return repository.findAll();
    }

    public Carro updateCarro(Carro carro){
        if(carro != null) {
             return repository.save(carro);
        }
        return null;
    }

    public Carro findCarroById(Integer id){
        try {
            return repository.findById(id).get();
        } catch (IllegalArgumentException illegal ){
            return null;
        } catch (NoSuchElementException ex){
            return null;
        }
    }

    public void deleteCarroById(Integer id){
        repository.deleteById(id);
    }
}
