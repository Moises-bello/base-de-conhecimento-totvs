---
content_hash: e2973fbbac01aebdbb4ba9b9b01ae45cad47715565d5099da181a981c481e38a
fetched_at: '2026-06-29T00:10:36.129870+00:00'
page_id: '531029409'
product: rm
source: tdn-rm
title: Planos de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531029409
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Sub-plano**
3. **Atenção**
4. **Telas utilizadas**

## **01. VISÃO GERAL**

Nesta função são cadastrados os planos que o Convênio possui e seus respectivos tipos de acomodação

## **02. SUB-PLANO**

Nesta funcionalidade, será possível cadastrar os Sub-Planos vinculados à Planos de Convênios previamente cadastrados.

## **03. ATENÇÃO**

A máscara definida neste campo será utilizada no momento do Registro de Internações e Registro de Atendimentos Externos. Na tela de Pedido de Exames para Pacientes Internos não será permitido alterar a máscara do código do usuário no convênio.  
Lembrando que a Mascara para ser somente de letra temos que colocar a letra L, somente numero # os dois a Letra A  
**Observação:**  
Convenio usa subplano: obedecer a mascara do subplano, caso marcado "utilizar mascara subplano" e "utiliza subplano"  
-Convenio não usa subplano: obedecer a mascara do plano, caso marcado "utilizar mascara plano" e desmarcado "usa subplano".  
A máscara do plano somente será utilizada se desmarcado "Utiliza subplano" e marcado "Utiliza máscara plano".  
Acessar um atendimento que já tenha cod.usuario preenchido, alterar a mascara e ao acessar o atendimento vai perder os dados caso não atenda a mascara (emite mensagem avisando que campo não atende a mascara).  
-Menu que fazem tratamento de mascara: atendimentos internos, externos e mudança de categoria do paciente. Verificar um atendimento que já tenha código de usuário convênio preenchido, conferindo como o sistema trata a mascara. Criar um novo atendimento conferindo como o sistema trata a máscara.

## **04. TELAS UTILIZADAS**

**PRINTS**
