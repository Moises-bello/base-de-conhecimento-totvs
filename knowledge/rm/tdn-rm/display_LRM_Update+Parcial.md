---
content_hash: 18cb6697e55b05da9f2bf4e8271803ad821a3fe9e64531d7c9217f7d7d9ac71d
fetched_at: '2026-06-29T00:08:46.355619+00:00'
page_id: '317003108'
product: rm
source: tdn-rm
title: Update Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/Update+Parcial
version: 3
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.17 da linha RM.

# Update Parcial

Atualiza um registro no dataserver parcialmente. Esse método pode ser acionado através de uma requisição do tipo PATCH e no corpo dessa requisição deve constar o json com os dados a serem alterados. Após a alteração o método retornará uma mensagem confirmando a operação ou mostrando os erros ocorridos.

## Exemplo de utilização

Método: PATCH

URL: <http://localhost:8051/rmsrestdataserver/rest/GlbDeptoData/1$_$1$_$99>

### Corpo da requisição

{  
    "EMAIL": "depto@[totvs.com.br](http://totvs.com.br)",  
    "ATIVO": "F"  
}

### Resposta da requisição

{  
   "messages": [],  
   "length": 1,  
   "data":    {  
      "id": "1$\_$1$\_$99",  
      "CODCOLIGADA": 1,  
      "CODFILIAL": 1,  
      "CODDEPARTAMENTO": "99",  
      "NOME": "ACD - Pró-Reitoria de Graduação",  
      "CONTATO": "José Marques",  
      "LOCALIZACAO": "Avenida Raja Gabaglia, 2664, 2º andar, Bairro Santa Lúcia, Belo Horizonte - MG",  
      "TELEFONE": "2122-9000",  
      "FAX": null,  
      "RAMAL": "9298",  
      "CODCOLCONTAGER": null,  
      "CODCONTAGER": null,  
      "ATIVO": "F",  
      "EMAIL": "depto@[totvs.com.br](http://totvs.com.br)"  
   }  
}
