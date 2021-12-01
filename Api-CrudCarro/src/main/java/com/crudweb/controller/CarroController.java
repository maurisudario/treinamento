package com.crudweb.controller;

import com.crudweb.model.Carro;
import com.crudweb.service.CarroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class CarroController {

    @Autowired
    CarroService service;

    @GetMapping("/carros/{id}")
    public ResponseEntity<Carro> getCarroById(@PathVariable Integer id){
        return ResponseEntity.ok().body(service.findCarroById(id));
    }

    @PostMapping("/carros/add")
    public ResponseEntity<Carro> saveCarro(@RequestBody Carro carro){
        return ResponseEntity.ok().body(service.saveCarro(carro));
    }

    @DeleteMapping("/carros/delete/{id}")
    public void deleteCarro(@PathVariable Integer id){
        service.deleteCarroById(id);
    }

    @PutMapping("/carros/update")
    public ResponseEntity<Carro> updateCarro(@RequestBody Carro carro){
        return ResponseEntity.ok().body(service.updateCarro(carro));
    }
}