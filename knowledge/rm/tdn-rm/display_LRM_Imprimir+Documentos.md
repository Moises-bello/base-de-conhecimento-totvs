---
content_hash: a1f7501a8825413e54a02684a8c54f845475dd15ec3bfc6b1fd02be2ce8782a3
fetched_at: '2026-06-29T00:09:24.807464+00:00'
page_id: '423938023'
product: rm
source: tdn-rm
title: Imprimir Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Imprimir+Documentos
version: 4
---

Utilize este processo para imprimir os movimentos selecionados através da seleção de relatórios. Será exibida uma janela de edição para preenchimento do tipo e do formato de relatório que deseja imprimir ou visualizar.   
  
**Tipo de Relatório**

**Movimento**: Permite selecionar apenas relatórios parametrizados como NOTA FISCAL

**Genérico**: Permite selecionar apenas relatórios parametrizados como GENERICO

**Duplicata**: Permite selecionar apenas relatórios parametrizados como DOCUMENTO.   
***Observação***: Este tipo de relatório estará disponível se no tipo de movimento estiver parametrizado para gerar lançamento financeiro (etapa "Fin – Faturamento") e na etapa "Mov – Impressão 2/2" estiver marcado o parâmetro para imprimir boleto. Assim, ao imprimir, o relatório será gerado automaticamente e o boleto será registrado online, conforme a documentação específica sobre o [Registro Online de Boletos](https://tdn.totvs.com/display/LRM/Registro+Online+de+Boletos).

**Fatura**: Permite selecionar apenas relatórios parametrizados como FATURA.  
***Observação***: Este tipo de relatório é utilizado apenas em movimentos do tipo 2(vendas). A opção estará disponível quando no tipo de movimento na etapa "Fin – Faturamento" o tipo de documento gerado for fatura.

Renumerar movimentos

A opção de renumerar movimentos estará disponível apenas se o tipo de movimento estiver parametrizado na etapa "Mov - Impressão 2/2" para tal.   
E só é permitida quando o tipo de relatório for "Movimento".   
Esta opção é utilizada para alterar a numeração e série de algum movimento para sua impressão.

Parametrização

A impressão de movimentos estará disponível se no tipo de movimento estiver parametrizado na etapa "Mov - Impressão 1/2" uma ação ao cadastrar movimento (diferente de não imprime).
