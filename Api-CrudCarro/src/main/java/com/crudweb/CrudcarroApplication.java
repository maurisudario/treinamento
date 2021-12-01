package com.crudweb;

import com.crudweb.model.Carro;
import com.crudweb.repository.CarroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CrudcarroApplication {
	public static void main(String[] args) {
		SpringApplication.run(CrudcarroApplication.class, args);
	}
}