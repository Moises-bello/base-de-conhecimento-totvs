---
article_id: 12075608640535
category: GPE - eSocial - Não Periódicos
content_hash: 18269f1ed357e055e0890efc574fad442c688bea20a4c4ca7e4f9b75aff51abc
fetched_at: '2026-06-28T22:45:06.090418+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - RH - Linha Protheus - GPE - eSocial - Código da
  Ocorrência: 180 ao transmitir não periódicos: O Vínculo Trabalhista não foi localizado'
type: support-article
updated_at: '2023-01-31T20:15:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12075608640535-RH-Linha-Protheus-GPE-RH-Linha-Protheus-GPE-eSocial-C%C3%B3digo-da-Ocorr%C3%AAncia-180-ao-transmitir-n%C3%A3o-peri%C3%B3dicos-O-V%C3%ADnculo-Trabalhista-n%C3%A3o-foi-localizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Codigo da ocorrência: 180 Descrição: O Vinculo Trabalhista nao foi localizado. Acao Sugerida: Utilize o evento de admissao para cadastramento do vinculo trabalhista.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**

A inconsistência é apresentada quando está tentando transmitir eventos não periódicos (S-2205, S-2206, etc) e o **Governo não localiza o vínculo trabalhista** (S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador) registrado no Portal do eSocial.

Em alguns casos, o vínculo trabalhista existe no Portal do eSocial e mesmo assim a inconsistência é retornada. Possivelmente, o registro de alteração está com alguma informação divergente como, por exemplo, a Matricula eSocial, CPF do trabalhador ou Tipo de Contrato.  
  
**Solução**Para solucionar essa ocorrência, realize as seguintes validações:**1)** Para os casos que **não foi localizado o registro no eSocial** será necessário enviar o evento de registro de admissão (S-2200) para o efetivo vínculo, para, em seguida, prosseguir com o envio da alteração cadastral ou contratual.

**2)** Registro de cadastramento inicial consta no Portal do eSocial  
O eSocial valida a data de alteração contratual para realizar a vinculação ao cadastro do trabalhador, mas se essa data for anterior a data que o funcionário inciou o vínculo, o eSocial não localizará as informações cadastrais. Dessa forma, será necessário ajustar a data de alteração para ser enviado ao eSocial.

**3)** Dados divergentes no XML  
Caso exista no XML um dado divergente do arquivo de admissão, como CPF ou Matricula, por exemplo, o eSocial não identificará o trabalhador pois essas informações são chaves primárias de identificação dos dados cadastrais. Sendo assim, confira os dados preenchidos no cadastro do Funcionário. Em seguida, gere o XML novamente e integre com o TAF para transmissão ao Governo.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
