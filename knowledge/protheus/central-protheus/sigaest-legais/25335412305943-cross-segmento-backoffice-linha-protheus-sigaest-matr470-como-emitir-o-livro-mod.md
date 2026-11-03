---
article_id: 25335412305943
category: SIGAEST - LEGAIS
content_hash: 71514405081a9640f846eba3d1230ade1380dd985ab9c5edd5a89d153576e8a1
fetched_at: '2026-06-28T22:38:51.754526+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR470 - Como emitir
  o livro modelo 3, registro controle da produção e estoque?
type: support-article
updated_at: '2024-08-01T17:05:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25335412305943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR470-Como-emitir-o-livro-modelo-3-registro-controle-da-produ%C3%A7%C3%A3o-e-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25335412282647) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como emitir o livro modelo 3, registro controle da produção e estoque?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**

Existe o relatório P3 - Registro de Controle de Producao e Estoque, é emitido pela rotina MATR470, segue abaixo mais informações

**Informações sobre o relatório MATR470:**

Recebe o nome oficial de **Registro de Controle da Produção e do Estoque** - Modelo 3.

Destina-se à escrituração dos documentos fiscais e dos documentos de uso interno do estabelecimento, correspondentes às entradas e saídas, produção e quantidades referentes aos estoques de mercadorias (Lei nº. 6.374/89, art. 67, § 1º, e Convênio de 15/12/70 - SINIEF, art. 72).

As informações fornecidas neste manual são exemplos. Consulte as fontes IOB e/ou Diários Oficiais disponíveis na sua cidade, para checar as informações.

Os lançamentos são feitos operação a operação, utilizando uma folha para cada espécie, marca, tipo e modelo de mercadoria, sendo lançados em quadros e colunas próprias.

Este livro pode ser substituído por fichas, a critério do fisco, sendo  organizadas por uma ficha índice.

A escrituração dos livros ou das fichas não pode sofrer atraso superior a 15 dias.

No módulo Livros Fiscais é possível emitir este documento dentro dos padrões estabelecidos por lei.

Este relatório ordena as informações por dia, não informando mão-de-obra

Lista os dados por intervalo de armazéns. É possível imprimir as informações de diversos armazéns em uma única impressão.

Para utilizar esta funcionalidade observe a configuração dos parâmetros da rotina

---

**Procedimentos**

Para emitir o relatório de Registro Kardex - Modelo 3:

1. No menu do Protheus basta seguir o caminho: Relatórios > Legais > Registro de Kardex Modelo 3  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25341042368663)
2. Em **Registro de Kardex Modelo 3**, clique em **Parâmetros,** observe os parâmetros:

* **Do Armazém?/Até o Armazém?**

Informe o intervalo de armazéns a ser considerado  para a apresentação dos dados.

|  |
| --- |
| ***Observação:***   * + Para empresas que trabalham com custo unificado por filial, (para mais detalhes consulte o parâmetro [MV\_CUSFIL](https://tdn.totvs.com/pages/viewpage.action?pageId=312165205)), as informações impressas neste relatório independem do número do armazém. Assim, para a impressão do relatório, informe o conteúdo "\*\*" (duplo asterisco).   + Os dados contidos no armazém, definidos pelo parâmetro [MV\_LOCPROC](https://tdn.totvs.com/pages/viewpage.action?pageId=312165149), devem ser impressos separadamente da movimentação dos demais armazéns. |

* **Lista Prods S/ Movim?**  
  Informe **Sim** para imprimir todos os produtos listados, ou **Não** para que o Sistema considere apenas os produtos que apresentem movimentações.
* A pergunta **Desconsiderar CFOPs** permite definir quais itens de **Notas Fiscais de Entrada** são desconsideradas no relatório para atender a legislação de alguns Estados em virtude de haver produtos destinados a **consumo** ou **ativo imobilizado** que não devem ser considerados no relatório.

3. Configure os demais parâmetros de acordo com a orientação do *help* de campo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25341189590039)

4. Confira as configurações e confirme a impressão.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25341166782999)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
