---
article_id: 38655973352215
category: MDT - Acidente de Trabalho
content_hash: a256b05b49d5000fbccf341c51488e2c879890aefc8e50090cd98d06704c996a
fetched_at: '2026-06-28T22:44:23.958115+00:00'
product: protheus
section_id: 360012070513
source: central-protheus
title: RH - Linha Protheus - MDT - Códigos do campo Objeto Causador não são apresentados
  na rotina de Acidentes
type: support-article
updated_at: '2026-02-26T11:20:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38655973352215-RH-Linha-Protheus-MDT-C%C3%B3digos-do-campo-Objeto-Causador-n%C3%A3o-s%C3%A3o-apresentados-na-rotina-de-Acidentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38655950821399) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao acessar a rotina de **Acidentes**, no módulo de Medicina do Protheus, os códigos do campo **Objeto Causador** não estão sendo exibidos.

**Ambiente**  
TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**  
Foi implementada uma validação nesse campo para que sejam exibidos apenas os códigos vinculados à **Tabela 14 do** **eSocial**, com o objetivo de evitar inconsistências na transmissão do evento **S-2210**.

**Solução**  
Para que os códigos corretos sejam apresentados, é necessário executar o Wizard do MDT, realizando a carga das tabelas conforme orientações disponíveis no link abaixo:

Tabelas: <https://tdn.totvs.com/display/PROT/MDT0028+Wizard+de+Importacao+eSocial>

[RH - Linha Protheus - MDT - eSocial - Para que serve e como utilizar a rotina Wizard MDT (MDTA891) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411512624151-RH-Linha-Protheus-MDT-eSocial-Para-que-serve-e-como-utilizar-a-rotina-Wizard-MDT-MDTA891-no-eSocial)

**Saiba Mais**  
[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
