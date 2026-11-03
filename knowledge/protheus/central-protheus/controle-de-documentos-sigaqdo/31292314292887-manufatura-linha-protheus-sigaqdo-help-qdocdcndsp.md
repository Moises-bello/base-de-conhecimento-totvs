---
article_id: 31292314292887
category: Controle de Documentos (SIGAQDO)
content_hash: 782a16fe50daf48027f8f6fe112b0995dfaf21061a56960009014efc85c806a2
fetched_at: '2026-06-28T22:42:29.159412+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDOCDCNDSP
type: support-article
updated_at: '2025-04-11T11:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31292314292887-Manufatura-Linha-Protheus-SIGAQDO-Help-QDOCDCNDSP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31292345035927) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar visualizar ou editar o documento na rotina **QDOC010 - Pesquisa de Localizadores / Texto em Documentos** é apresentado o *help* **QDOCDCNDSP - O usuário corrente não tem acesso para edição ou visualização do documento selecionado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões.  
  
**Causa**Esse incidente ocorre nas situações:

* Quando o usuário **não está parametrizado para ser o responsável** do documento ou é o responsável pelo documento, porém **não tem permissão de editar** o mesmo;
* Quando o usuário não está parametrizado para ser o responsável do documento já distribuído e o parâmetro **MV\_QLIBLEI - Define se a Leitura do Documento poderá ser feita por todos os usuários** está com conteúdo igual a **N - Não**;
* Quando o usuário **não está parametrizado para ser o responsável** do documento e **ainda não  foi distribuído**.
* Quando o **documento é sigiloso**, somente usuários responsáveis poderão visualizar e editar;
* Quando o documento está **obsoleto**.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Avaliar **permissão de editar** o documento na rotina **QDOA020 - Tipos de Documentos;**2. Verificar se o parâmetro **MV\_QLIBLEI** está com conteúdo igual a **S- Sim**;  
3. Confirmar se o documento já foi distribuído e está em leitura. O parâmetro **MV\_QLIBLEI** atua  
permitindo visualização somente em documentos cuja distribuição já ocorreu;  
4. Avaliar se o documento é **Sigiloso**, se positivo, somente o usuário responsável poderá visualizar ou  
editar;  
5. Se o documento for **obsoleto**, será verificado se o usuário em questão possui a **permissão 96 - Consulta doctos. obsoletos** marcada no **SIGACFG - Configurador**.  
  
**Saiba mais**  
Na documentação a seguir mais informações sobre Documento Sigiloso: [Manufatura - Linha Protheus - SIGAQDO - Documento Sigiloso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13163882240791-Manufatura-Linha-Protheus-SIGAQDO-Documento-Sigiloso)
