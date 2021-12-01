package com.crudweb.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class WebController {

    @RequestMapping(method = RequestMethod.GET, path = "/index")
    public String index(){
        return "templates/index";
    }

    @RequestMapping(method = RequestMethod.GET, path = "/buscarCarro")
    public String buscarCarro(){
        return "buscarCarro";
    }
}
