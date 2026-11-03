---
article_id: 4413537068183
category: RH - Integração de Titulo
content_hash: ca0c37beac4d1a00f90d25ccc3d0812b41bc7e621ecb61aa39982065046ec666
fetched_at: '2026-06-28T22:43:37.237080+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada PE GP650CFO Grava Dados Fornecedor
type: support-article
updated_at: '2025-07-18T14:02:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413537068183-RH-Linha-Protheus-GPE-Ponto-de-Entrada-PE-GP650CFO-Grava-Dados-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558595459479) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do ponto de entrada PE GP650CFO

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

#### **Descrição**

Ponto de entrada criado antes da execução da "ExecAuto" do cadastro de fornecedores automático na geração de títulos com o objetivo de adicionar mais campos ao "array" passado para o cadastro de fornecedores para serem levados mais dados do funcionário para o novo fornecedor cadastrado.

**Segue o trecho do fonte que chama o ponto de entrada:**

-------------------------------------------------------------------------------------------------

aDadosAuto:= {{'A2\_COD'    , cCpoFornec      , Nil},;

                        {'A2\_LOJA'   , cLoja               , Nil},;

                        {'A2\_NOME'   , SRA->RA\_NOME       , Nil},;

                        {'A2\_NREDUZ' , SRA->RA\_NOME    , Nil},;

                        {'A2\_END'    , SRA->RA\_ENDEREC , Nil},;

                        {'A2\_EST'    , SRA->RA\_ESTADO  , Nil},;

                        {'A2\_MUN'    , SRA->RA\_MUNICIP , Nil},;

                        {'A2\_TIPO'   , 'F'             , Nil},;

                        {'A2\_CGC'    , SRA->RA\_CIC     , Nil},;

                        {'A2\_BAIRRO' , SRA->RA\_BAIRRO  , Nil}}

If lGP650CFO

aDadosPE := ExecBlock("GP650CFO",.F.,.F.,aDadosAuto)

If ValType(aDadosPE) == "A" .And. Len(aDadosPE) >= 10

aDadosAuto := aDadosPE

EndIf

EndIf

//Cadastra um novo Fornecedor

MSExecAuto({|x, y| MATA020(x, y)},aDadosAuto, 3)

-------------------------------------------------------------------------------------------------

**IMPORTANTE:**

O ponto de entrada deve **SEMPRE** retornar um array que contenha os dados já existentes no array aDadosAuto, passado como referência, mais os campos que o usuário desejar adicionar, com seu devido conteúdo, conforme exemplo mais abaixo. O array retornado deve **SEMPRE** retornar no mínimo os campos já existentes no parâmetro passado como referência, não podendo ser retirado nenhum campo, apenas adicionado.

#### **Ponto de Entrada - Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'  
  
User Function GP650CFO()  
    Local aCampos := PARAMIXB  
      
    aAdd(aCampos,{'A2\_COD\_MUN' , SRA->RA\_CODMUN  , Nil})  
Return aCampos

**BASE TDN*****:** <https://tdn.totvs.com/display/public/PROT/PE+GP650CFO+Grava+Dados+Fornecedor>*

***Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)*
