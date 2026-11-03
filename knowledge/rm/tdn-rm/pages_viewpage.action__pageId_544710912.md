---
content_hash: 7e47ea62b7de0b60e00b11cabe60202e8e785bf3f6816fbf186377cd9463fc84
fetched_at: '2026-06-29T00:10:38.691909+00:00'
page_id: '544710912'
product: rm
source: tdn-rm
title: Enviei um evento através do middleware, porém não recebo retorno do governo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544710912
version: 5
---

# Objetivo:

---

       O objetivo deste documento é orientar como proceder caso tenha enviado algum evento ao governo, porém ao realizar a atualização do status, não existe retorno por parte do governo, o evento permanece com status "3 - Enviado".

---

0Passo 1

Verifique se o ambiente do governo está estável. É possível fazer um acompanhamento através do portal do esocial, no [semáforo](http://portal.esocial.gov.br/semaforo).

Passo 2

Verifique se não existem bloqueios internos através de firewall ou políticas de proxy na rede da empresa.

Para consultar os eventos, é necessário possuir permissão para acesso às url's:

Ambiente Produção: https://webservices.consulta.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc

Ambiente Produção Restrita:https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc

Passo 3

1 - Para esta situação dos eventos que estão com status "3 - Enviado", pode ser necessário a atualização do TSS;

2 - Acesse a documentação abaixo para atualização do binário e do arquivo RPO na pasta de instalação do TSS:  
[Atualizando o Binário e o RPO do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025392671-MP-TSS-Atualiza%C3%A7%C3%B5es-do-TSS-Totvs-Sped-Service)

3 - O próximo passo é a atualização da URL do TSS. Segue documentação:  
[Atualizando URL TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS)  
   
4 - Localize outra seção [**GENERAL**], ajuste a chave **MaxStringSize** para o valor 20:

**Exemplo:**  
**[General]**  
INSTALLPATH=C:\TOTVS 12\totvssped  
CONSOLELOG=1  
BuildKillUsers=1  
**MaxStringSize=20**

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.26 |
| 12.1.27 |

falsefalse

**Status: Concluido**

false

**Data: 24/03/2020**

false

**Autor:**
