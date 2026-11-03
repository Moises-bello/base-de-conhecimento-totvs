---
article_id: 360036064914
category: MDT - eSocial
content_hash: edfc06051f4a8e52d38abe3bf3d077fd823cf88ada418ee7bcf8798364b3cb9c
fetched_at: '2026-06-28T22:44:29.405635+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2245 - Ao tentar cadastrar um instrutor
  no modulo SIGAMDT ou SIGATRM o sistema apresenta a mensagem que os campos CPF Instruto,
  Form. Instru, CBO Instruto, Nac. Instrut são obrigatórios
type: support-article
updated_at: '2025-07-31T14:12:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036064914-RH-Linha-Protheus-MDT-eSocial-S-2245-Ao-tentar-cadastrar-um-instrutor-no-modulo-SIGAMDT-ou-SIGATRM-o-sistema-apresenta-a-mensagem-que-os-campos-CPF-Instruto-Form-Instru-CBO-Instruto-Nac-Instrut-s%C3%A3o-obrigat%C3%B3rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27604967135639)**Tempo aproximado para leitura: 00:01:00 min **Ocorrência**Ao tentar cadastrar um instrutor no modulo Medicina e Segurança do Trabalho ou Treinamento o sistema apresenta a mensagem que os campos **CPF Instruto**, **Form. Instru**, **CBO Instruto**, **Nac. Instrut** são obrigatórios.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095387894)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
 **Causa**Os campos obrigatórios para geração do evento S-2245 (Treinamento) não foram preenchidos..  
 **Solução**Quando não preenchido o campo matricula, ou seja, o instrutor não é funcionário da empresa é necessário o preenchimento desses campos (**CPF Instruto**, **Form. Instru**, **CBO Instruto**, **Nac. Instrut)** que será utilizado no evento S-2245 do eSocial. Para verificar o cadastro do instrutor acesse no modulo SIGAMDT o caminho: Atualizações > Treinamento > Instrutor.

* Caso deseje que o sistema apenas emita o aviso sem bloquear a inclusão altere o parâmetro **MV\_NG2AVIS** para 0 (emite aviso).
* Caso deseje desabilitar a integração do **SIGAMDT** com **TAF** altere o parâmetro **MV\_NG2ESOC** para 2.  
  Atenção: A entrega dos eventos SST foram prorrogadas pelo governo não havendo a necessidade de manter esse parâmetro ativado. Entretanto quando as entregas dos eventos SST passarem a ser obrigatórias não recomendamos manter o parâmetro desabilitado. Para acessar o novo cronograma do eSocial clique no artigo: [MP - MDT - eSocial - Novo calendário (cronograma) de entrega de eventos SST (Medicina e Segurança do Trabalho), portarias RFB/SEPRT nº 76 e 77](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058275933)

**Saiba Mais**[Artigos MDT - eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial-Protheus)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
