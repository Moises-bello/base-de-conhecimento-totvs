---
content_hash: abd4ad595346254ef8890b0e8c1657fa7e6ee670c75ec1d2a9750f683a3586eb
fetched_at: '2026-06-29T00:05:53.771530+00:00'
page_id: '1070836652'
product: rm
source: tdn-rm
title: Lançamentos de Outros\Debito - Diferencial de Alíquota - Mais detalhes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070836652
version: 2
---

## **Insere Lançamentos Diferencial Alíquota**

Conforme decreto **45.490/2000 do RICMS SP**, o diferencial de alíquota deve ser lançado como Outros Débitos e Créditos nos livros dos contribuintes. Deverão ser gerados dois lançamentos, um referente a Outros Débitos com o valor da base de cálculo do diferencial de alíquota aplicando a alíquota do Estado e outro referente a Outros Créditos, com a alíquota do diferencial.

**Exemplo:**

Débito: 1000,00 x 12% = 120,00

Crédito: 1000,00 x 6% = 60,00

No encerramento do período, o comportamento seria o mesmo que gerar um único débito a 60,00.

### Período:

Informe o período para a geração dos Lançamentos Outros Débitos e Créditos

### Classificação Débito / Classificação Crédito

Informe a classificação de acordo com as tabelas/quadros disponibilizados pela Secretaria da Fazenda será utilizada na [GIA SP.](http://idh_pastaoutrasinformacoesgiasp.htm/)

Ao clicar em Gerar, o sistema estará selecionando todos os Lançamentos Fiscais de entrada CFOP's (1.### e 2.###) com diferencial de alíquota maior que zero. Os Lançamentos Fiscais devem estar associados a naturezas FISCAIS e não podem se encontrar cancelados ou estornados. A partir destes lançamentos, o sistema estará calculando os valores a débito e a crédito que serão utilizados na geração dos lançamentos de outros débitos e créditos.

**Observação:**

O parâmetro "Considera Dif. Alíquota - Outros Débitos" totaliza o diferencial de alíquota como débito no Livro Resumo de Apuração do ICMS.

Para os contribuintes de São Paulo este parâmetro deverá estar desabilitado, visto que, devem ser gerados dois lançamentos, um a débito e outro a crédito.
