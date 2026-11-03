---
content_hash: 2a2b63178596a317a733fec1dc38b4b7b9686f560c70be4d474306b85764bf6d
fetched_at: '2026-06-29T00:12:14.059576+00:00'
page_id: '963027603'
product: rm
source: tdn-rm
title: 'Reforma Tributária: Cadastro de Tributos'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963027603
version: 13
---

**Importante:** Esta documentação complementa o conteúdo disponível em [Cadastro de Tributos](https://tdn.totvs.com/display/public/LRM/Cadastro+de+Tributos) e traz orientações específicas para a criação dos novos tributos exigidos pela Reforma Tributária.

## Objetivo

Orientar o cliente na criação dos novos tributos necessários para a operacionalização da Reforma Tributária, garantindo que o sistema esteja preparado para a apuração correta do **IBS Estadual**, **IBS Municipal**, **IBS Consolidado** e **CBS**.

## O que deve ser feito

Para **cada coligada ativa**, o cliente deve garantir que os seguintes tributos estejam cadastrados no sistema com as características corretas:

### IBS\_UF (IBS Estadual)

| Característica | Valor Esperado |
| --- | --- |
| Tipo de Alíquota | Variável |
| Abrangência | Estadual |
| Tipo do Tributo | IBS |
| Incidência | Ambos |
| Procurar Alíquota no | Cadastro de Vigência |

*Observação: A sigla do tributo pode variar. O importante é que todas as propriedades acima estejam corretamente configuradas.*

### IBS\_Mun (IBS Municipal)

| Característica | Valor Esperado |
| --- | --- |
| Tipo de Alíquota | Variável |
| Abrangência | Municipal |
| Tipo do Tributo | IBS |
| Incidência | Ambos |
| Procurar Alíquota no | Cadastro de Vigência |

### IBS (Consolidado)

| Característica | Valor Esperado |
| --- | --- |
| Tipo de Alíquota | Variável |
| Abrangência | Estadual/Municipal |
| Tipo do Tributo | IBS |
| Incidência | Ambos |
| Procurar Alíquota no | Cadastro de Vigência |

*Observação: Este tributo será utilizado para agrupar a apuração do IBS\_UF e do IBS\_Mun. A Validação de Período de Apuração aberto/encerrado se dará por este tributo. O cadastro é único por coligada, o sistema não permite o cadastro duplicado deste tributo.*

### CBS (Contribuição sobre Bens e Serviços)

| Característica | Valor Esperado |
| --- | --- |
| Tipo de Alíquota | Variável |
| Abrangência | Federal |
| Tipo do Tributo | CBS |
| Incidência | Ambos |
| Procurar Alíquota no | Cadastro de Vigência |

## Onde cadastrar?

O cadastro deve ser feito no menu:  
**TOTVS Backoffice | Linha RM > Gestão Fiscal > Cadastros > Tributos**

## Dúvidas frequentes

**1. Posso usar qualquer nome para o tributo?**  
Sim, desde que todas as características estejam conforme descritas acima.

**2. Preciso cadastrar os tributos mesmo se minha empresa ainda não estiver no regime de IBS/CBS?**  
Sim. O cadastro antecipado é importante para testes, validações e integração com demais cadastros fiscais.

**3. O sistema já cria esses tributos automaticamente?**  
Não. O cadastro é manual e deve ser feito considerando a estrutura de cada coligada.

]]>
