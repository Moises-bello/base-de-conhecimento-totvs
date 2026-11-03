---
content_hash: f195cd231e14da228fef921967a43a4d5a49cd596bd68c15e40f9ffd11153450
fetched_at: '2026-06-29T00:12:14.224765+00:00'
page_id: '967104711'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Hierarquia por Posição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967104711
version: 7
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Hierarquia por Posição |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11811](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11811) |

## **02.** **RELEASES**

* 12.1.2410.270
* 12.1.2502.173
* 12.1.2506.117 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar o envio das informações dos chefes com base na parametrização de Hierarquia/Posição cadastrada no TOTVS Gestão de Pessoas, no contexto da integração entre a Folha de Pagamento e o sistema de Ponto Web (Ahgora).

## **04. SOLUÇÃO**

Foi implementado o envio dos chefes buscando as informações parametrizadas no módulo Hierarquia/Posição no TOTVS Gestão de Pessoas.

No momento do envio dos colaboradores para a Ahgora será enviado o chefe na tag **"nome\_chefia"**.

Para visualização do organograma acesse o menu TOTVS Gestão de Pessoas | Valorização | Organograma  e conferência dos chefes enviado, conforme demonstrado abaixo:

**Json enviado para o Ponto Web (Ahgora).**

{  
  "dataAdmissao": "2011-05-01",  
  "matricula": "100082",  
  "nome": "RICARDO DA SILVA GONÇALVES",  
  "pis": "111111111111",  
  "regimeTrabalho": "CLT",  
  "bate\_ponto": "Ponto Livre",  
  "cargo": "00021-Atendente",  
  "dataCargo": "2011-05-01",  
  "carga\_horaria": "220",  
  "centroCusto": null,  
  "cnpj": "11111111111111",  
  "codInterno": "1|00082",  
  "cpf": "11111111111",  
  "ctps": "56986/0056/MG",  
  "dataCnpj": null,  
  "dataDemissao": null,  
  "dataNascimento": "1992-02-14",  
  "departamento": "01.02-COM - Depto Comercial",  
  "email": "monica@[totvs.com.br](http://totvs.com.br)",  
  "email\_chefia": "monica@[totvs.com.br](http://totvs.com.br)",  
  "escala\_padrao": "10001",  
  "lastChangeDefaultSchedule": "2011-04-01",  
  "localizacoes": null,  
  "matricula\_chefia": "100050",  
  "matricula\_esocial": null,  
  **"nome\_chefia": "GEMA MATTOLI DE MENEZES",**  
  "rg": "123.456",  
  "sem\_pis": false,  
  "sexo": "F",  
  "telefone": "123456",  
  "codSindicato": "0001",  
  "data\_troca\_elegibilidade\_ponto": null,  
  "matricula\_anterior": "",  
  "custo\_da\_hora": "2,25",  
  "financeiro": {  
    "salario": "495,00"  
  }  
}

**Tela do chefe enviado para o Ponto Web (Ahgora).**

## **05****. DOCUMENTAÇÃO**
