package com.crudweb.model;

import javax.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "carros")
public class Carro {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    @Column (name = "nome_carro")
    private String nomeCarro;
    @Column (name = "marca_carro")
    private String marcaCarro;
    @Column (name = "valor_carro")
    private double valorCarro;
    @Column (name = "cilindradas")
    private int cilindradas;
    @Column (name = "ano_lancamento")
    private int anoLancamento;

    public String getNomeCarro() {
        return nomeCarro;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setNomeCarro(String nomeCarro) {
        this.nomeCarro = nomeCarro;
    }

    public String getMarcaCarro() {
        return marcaCarro;
    }

    public void setMarcaCarro(String marcaCarro) {
        this.marcaCarro = marcaCarro;
    }

    public double getValorCarro() {
        return valorCarro;
    }

    public void setValorCarro(double valorCarro) {
        this.valorCarro = valorCarro;
    }

    public int getCilindradas() {
        return cilindradas;
    }

    public void setCilindradas(int cilindradas) {
        this.cilindradas = cilindradas;
    }

    public int getAnoLancamento() {
        return anoLancamento;
    }

    public void setAnoLancamento(int anoLancamento) {
        this.anoLancamento = anoLancamento;
    }
}
