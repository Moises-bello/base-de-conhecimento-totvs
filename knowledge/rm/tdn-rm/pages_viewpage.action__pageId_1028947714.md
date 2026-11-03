---
content_hash: 22e89d1f6246bebe75375fed7bdfd3af80ff2363c108a79aa65bf45f6586e9ce
fetched_at: '2026-06-29T00:05:48.783126+00:00'
page_id: '1028947714'
product: rm
source: tdn-rm
title: DT - Integração Folha X ATS - Atração de Talentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1028947714
version: 13
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração Folha X ATS - Atração de Talentos |
| País: | Brasil |
| Épico: | [DRHROTRM-15754](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15754 "View this issue") |

## **02. VERSÃO**

* 12.1.2506.275
* 12.1.2510.194
* 12.1.2602. e superiores

## **03. S****ITUAÇÃO/REQUISITO**

A integração entre o sistema TOTVS Folha de Pagamento (RM) e TOTVS Atração de Talentos (ATS) representa um avanço significativo na digitalização do RH, eliminando processos manuais e a redigitação de informações. Utilizando a tecnologia SmartLink, a comunicação entre as plataformas ocorre de forma automatizada e segura: assim que a contratação de um candidato é aprovada no ATS, seus dados são enviados para uma fila de integração. No RM, um consumer (serviço de consumo) monitora essa fila, processa as informações e as armazena em uma tabela de transição.

O grande diferencial operacional desta melhoria está na etapa final da admissão. No módulo de Folha de Pagamento, ao cadastrar um novo funcionário, o usuário conta com a funcionalidade "Localizar Pessoa", que agora está vinculada diretamente à tabela alimentada pelo ATS. Isso permite que os dados do candidato sejam importados instantaneamente, garantindo agilidade no onboarding, redução de erros de digitação e total conformidade com os dados validados durante o processo seletivo.

## **04.****SOLUÇÃO**

Foi implementada no sistema a integração entre o **TOTVS Folha de Pagamento (RM)** e o **TOTVS Atração de Talentos (ATS)**, realizada por meio do **Smartlink.**

Com essa melhoria, foi disponibilizada uma nova tela para localização do candidato.

Acesse o menu Administração de Pessoal | Funcionário | Aba Identificação e, em seguida, selecione **Localizar Pessoa / Registro Preliminar**.

false⚠️ ATENÇÃO:

* É uma premissa da integração que o campo **CNPJ** esteja devidamente preenchido no cadastro da empresa no **ATS**, pois a **Folha de Pagamento** identifica a coligada/empresa por meio dessa informação. Caso o CNPJ não esteja informado, o candidato **não será integrado**. Para mais detalhes sobre como preencher o CNPJ no ATS, acesse o [link](https://tdn.totvs.com/pages/viewpage.action?pageId=641167075).
* No momento, a integração ainda **não atende clientes que utilizam requisição**. Assim que essa funcionalidade estiver disponível, comunicaremos por meio das nossas novidades.

## **05.** **TABELAS UTILIZADAS**

* PATSCANDIDATO

## **06. DEMAIS INFORMAÇÕES**
