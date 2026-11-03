---
article_id: 36306740356503
category: RH - Rescisão
content_hash: d399be84022d819e42d377342810bd4be05b934ed6b401d44edadd42e0c8b3c2
fetched_at: '2026-06-28T22:43:50.845888+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Quais verbas são consideradas na rescisão para
  calcular a margem do eConsignado
type: support-article
updated_at: '2025-11-17T19:12:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36306740356503-RH-Linha-Protheus-GPE-Quais-verbas-s%C3%A3o-consideradas-na-rescis%C3%A3o-para-calcular-a-margem-do-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36306755557015) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como podemos saber quais são as verbas na rescisão que o sistema está utilizando para calcular a margem do eConsignado para desconto na rescisão?

**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12

**Solução**  
A remuneração disponível, para fins de cálculo da margem consignável, refere-se à soma das verbas com incidência de contribuição previdenciária (**INSS**), ou seja, somente valores de natureza remuneratória — que são sujeitos ao desconto do INSS — podem ser utilizados para calcular o limite de 35% para o desconto da parcela consignada.

As verbas que entram no cálculo da margem consignável na rescisão incluem:

* Saldo de salário (pelos dias efetivamente trabalhados)
* 13º salário proporcional
* Aviso prévio indenizado (caso no cadastro da verba esteja SIM para INSS, aba incidências)
* Horas extras apuradas e devidas
* Comissões, adicionais e prêmios habituais, desde que sujeitos ao INSS.

\*\* Memoria de cálculo do sistema

Verbas de **provento** com **sim para INSS** + verbas informadas no **P\_ADICONS** - **INSS** - **IR** - verbas de **desconto** com **sim para INSS** - verbas informadas no**P\_DEDCONS**  
  
Para identificar as verbas que o sistema utiliza no cálculo da margem para desconto na rescisão, é necessário verificar as verbas que contém incidência para INSS que são apresentadas no cálculo.

A fim de facilitar esta conferência, acesse pelo menu do SIGAGPE: Atualizações > Definições de Cálculo > Verbas.  
Selecione a opção **filtro** no canto superior direito, e clique em criar filtro.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36306755557143)  
  
Selecione as opções INSS igual a S-Sim e depois em adicionar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36306740345751)  
  
Para confirmar a criação do filtro, clique em salvar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36306740346007)  
  
  
Selecione a opção do filtro recém criado e depois em Aplicar Filtros Selecionados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36306740346391)  
  
Desta forma, serão apresentadas em tela somente as verbas que estejam com S- Sim para INSS.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Cálculo eConsigando em rescisãoRH - Linha Protheus - GPE - Cálculo eConsigando em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32327889957271-RH-Linha-Protheus-GPE-C%C3%A1lculo-eConsigando-em-rescis%C3%A3o)

Consultoria de Segmentos Totvs (item 3.6): <https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-2.NormasApresentadaspeloCliente>

Central de Faq's [eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

Manual Protheus [Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=944703898)
