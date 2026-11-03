---
article_id: 1500009637621
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 793867514996fd95163dc357b65b7efa23cf71db3e2fa3a4d596cad3f3a46a08
fetched_at: '2026-06-28T22:39:56.417919+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Dados da
  Obra no XML (Emissor Municipal)
type: support-article
updated_at: '2026-02-09T20:10:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009637621-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Dados-da-Obra-no-XML-Emissor-Municipal
---

**Dúvida**  
Como destacar no XML os dados da obra através do parâmetro MV\_XMLOBRA?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**  
O destaque dessas informações irá depender se a prefeitura em questão possui tags próprias para tal, exemplo da de São Paulo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014785622)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014785822)  
  
Através do parâmetro **MV\_XMLOBRA** é definido quais informações devem ser montadas pelo remessa do Protheus e consequentemente caso a prefeitura tenha as tags próprias (print acima), na conversão o TSS irá monta-las.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416271298327)

O parâmetro MV\_XMLOBRA possibilita ao usuário criar campos adicionais no pedido de venda (SC5), para dados referente a obra para que essas informações sejam transmitidas na NFS-e.  
  
No parâmetros os campos criados na tabela SC5 – Pedido de Venda, deverão seguir a seguinte ordem:

Posição 1: Logradouro Da Obra;

Posição 2: Complemento do Endereço da Obra;

Posição 3: Numero do End. da Obra;

Posição 4: Bairro da Obra;

Posição 5: Cep da Obra;

Posição 6: Cod Municipio da Obra;

Posição 7: Nome Municipio da Obra;

Posição 8: Estado da Obra;

Posição 9: Codigo do Pais da obra;

Posição 10: Nome do Pais da Obra;

Posição 11: Numero Art. da Obra;

Posição 12: Numero do CEI da Obra;

Posição 13: Numero do Projeto da Obra;

Posição 14: Numero da Matricula da Obra.

Posição 15: Numero do Encapsulamento  
  
Exemplo:   
Na necessidade de destacar o conteúdo 11, 12 e 15 o parâmetro deverá estar da seguinte maneira abaixo:  
  
{,,,,,,,,,,'C5\_NUMART','C5\_NUMCEI',,,'C5\_NUMENCAP'}  
  
Considerando que tenham sido criados os campos na tabela SC5: *C5\_NUMART, C5\_NUMCEI e C5\_NUMENCAP.*  
  
Para maiores detalhes sobre o parâmetro MV\_XMLOBRA, consulte o [Documento Técnico](http://tdn.totvs.com/pages/viewpage.action?pageId=187533341).
