---
article_id: 40653605488663
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5a8bfa961acb26ce17a3b7bca7419923096aab6acd3b2ca209641e21ac317f79
fetched_at: '2026-06-28T22:38:58.523883+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Nota de Débito
  do tipo 7 Perda em Estoque
type: support-article
updated_at: '2026-05-26T15:58:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40653605488663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Nota-de-D%C3%A9bito-do-tipo-7-Perda-em-Estoque
---

A emissão da Nota de Débito por Perda em Estoque, conforme a Reforma Tributária (Lei Complementar nº 214/2025), deve usar finalidade 6, tipo 07 e CFOP 5.927 para estornar créditos de IBS e CBS em perdas, furtos ou deteriorações. Para produtos de revenda, é obrigatório referenciar a NF-e de entrada, enquanto para produção própria, não é necessário. Em casos de transição tributária, devem ser emitidos dois documentos distintos para créditos da reforma e tributos tradicionais.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40653542568471) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**

Como emitir a Nota de Débito por Perda em Estoque no contexto da Reforma Tributária (IBS e CBS) para produtos de revenda e de fabricação própria?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - A partir da release 12.1.2510  
  
**Solução**

A Reforma Tributária, instituída pela Lei Complementar nº 214/2025, introduziu as novas finalidades de emissão da NF-e estabelecidas pela Nota Técnica 2025.002-RTC, que incluem a "Nota de Débito". O documento de Nota de Débito com tipo focado em "Perda em estoque" tem o objetivo de formalizar o estorno de créditos de IBS e CBS apropriados inicialmente, sempre que o bem adquirido ou produzido for objeto de perda, perecimento, deterioração, roubo, furto ou extravio.

![Perda em Estoque 01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/40744403544727)

Para formalizar a perda e reverter o crédito tributário, a emissão do documento fiscal deve contemplar os seguintes parâmetros estruturais:

* **Finalidade de Emissão (finNFe)**: A nota deve possuir a finalidade 6 = Nota de Débito;
* **Tipo de Nota de Débito (tpNFDebito)**: O campo deve ser preenchido com 07 = Perda em estoque;
* **CFOP**: Utilize o código 5.927, que representa o lançamento efetuado a título de baixa de estoque;
* **Destinatário**: Os dados informados devem ser do próprio emitente da nota, utilizando o mesmo CNPJ da empresa;
* **Impostos e Valores**: A nota deve ser emitida para a recomposição de impostos da reforma.

![Perda em Estoque 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/40744403550999)

**Passos**

Os procedimentos de referenciamento e apuração variam de acordo com a origem do material, além dos cuidados exigidos no período de transição dos tributos:

1. **Para Produtos de Revenda (Adquiridos de Terceiros):**

   * Emita a Nota de Débito com a finalidade de emissão 6 e o CFOP 5.927;
   * Referencie obrigatoriamente o documento fiscal de entrada (NF-e de aquisição), para garantir a rastreabilidade da operação e possibilitar a vinculação ao crédito apropriado anteriormente.
2. **Para Produtos Acabados (Produção Interna):**

   * A Nota de Débito pode ser emitida sem referenciar a NF-e de origem, pois a Regra de Validação VC02-10 da Nota Técnica 2025.002-RTC não torna obrigatório o referenciamento para o tipo 07 (Perda em estoque);
   * Considere que o estorno não se restringe ao produto final, abrangendo também os créditos vinculados aos serviços e insumos consumidos em sua produção;
   * Para determinar o valor exato a ser estornado na ausência de rastreabilidade de lote, aplique o critério do artigo 48 da Resolução CGIBS nº 6/2026: utilize os créditos das aquisições mais recentes (ordem cronológica inversa) até alcançar a quantidade necessária correspondente à baixa;
3. **Para Cenários de Incidência Simultânea (Período de Transição):**

   * Em operações onde o produto sofreu incidência dos tributos atuais (ICMS, PIS, COFINS, IPI) e dos tributos da reforma (IBS e CBS), é necessário emitir dois documentos distintos:

     + **Nota 1**: Emita a Nota de Débito exclusivamente para o estorno dos créditos de IBS e CBS, evitando a rejeição 1001 (NF-e com finalidade de débito ou crédito somente para IBS/CBS).
     + **Nota 2**: Emita uma NF-e padrão de Ajuste (Finalidade 3) e CFOP 5.927 para formalizar a baixa de estoque e suportar os estornos dos impostos tradicionais (ICMS, PIS, COFINS, IPI) de forma escritural.

**Essa rotina possui Execauto?**

[*Notas de Débito (MATA600) - ExecAuto*](https://tdn.totvs.com/x/4cg1Pg)

**Saiba mais**:

[*Como configurar a rotina MATA600 Notas de Débito?*](https://tdn.totvs.com/x/MZ5qP)

[*Reforma Tributária - Novas Finalidades de Emissão da NF-e*](https://tdn.totvs.com/x/pCqWOg)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
