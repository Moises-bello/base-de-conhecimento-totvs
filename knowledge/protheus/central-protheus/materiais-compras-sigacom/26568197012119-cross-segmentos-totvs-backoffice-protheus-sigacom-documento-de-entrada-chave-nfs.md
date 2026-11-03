---
article_id: 26568197012119
category: Materiais - Compras (SIGACOM)
content_hash: 55a9e370591deeb29f678df96fb118a908ca8621d15ecb6a8fd9707e8a7183ce
fetched_at: '2026-06-28T22:41:17.375300+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  Chave NFS com 50 posições
type: support-article
updated_at: '2026-06-23T18:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26568197012119-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-Chave-NFS-com-50-posi%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26568196998935) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
No documento de entrada, em qual campo devemos preencher a chave NFS com 50 posições?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) – A partir da versão 12.00

**Solução**  
Para que no documento de entrada seja informada a chave NFS com 50 posições, é necessário :

**1-)** Criar o parâmetro: [**MV\_CHVNFS**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=864983270) ( se a release em uso for anterior a 2410 ).

**2-)** Aplicar o pacote que consta no link abaixo, para atualização dos fontes :

**release 22.10 -** ( somente clientes com garantia estendida em uso ) <https://suporte.totvs.com/portal/p/10098/download?e=1162820>

**release 23.10 -** https://suporte.totvs.com/portal/p/10098/download?e=1162821

**release 24.10 -** <https://suporte.totvs.com/portal/p/10098/download?e=1162823>

**3-)** O campo em uso é o já existente no dicionário padrão :

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26568212248343)**

**4-)** O campo **F1\_CODNFE** só deverá  ser preenchido quando, as espécies da nota de entrada forem :

**NFS, NFSE, NFSC e NFST**, ou seja, as espécies correspondentes às notas de entrada de aquisição de serviços.

**5-)** Necessário ter o TSS também configurado para acesso à validação da chave eletrônica para notas de serviço.

**6-)** Criado parâmetro [**MV\_VCHVNFS**](https://tdn.totvs.com/pages/releaseview.action?pageId=1068941204) para validação das informações do cabeçalho do documento de entrada com a chave da nota de serviço, informada no campo F1\_CODNFE.

**Pacote para ser aplicado :  Para releases do Protheus, já expiradas, antes de aplicação do pacote, verificar garantia estendida.**

12.1.2310:<https://r.totvs.io/p/1253440> ;

12.1.2410:<https://r.totvs.io/p/1253441> ;

12.1.2510:<https://r.totvs.io/p/1253442> ;

Caso tenha alguma dúvida no tocante a essa situação, favor acionar a equipe do SPED/TSS através de ticket.

***Saiba Mais :***

[Preenchimento chave NFS no documento de Entrada](https://tdn.totvs.com/pages/releaseview.action?pageId=864980227)

[Página Centralizadora do Compas](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
