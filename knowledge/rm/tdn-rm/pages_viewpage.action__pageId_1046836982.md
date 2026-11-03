---
content_hash: 219afaa5161eef8f1db4b0be19e56393c8d84eca05eea460f8a01e1fc3455b64
fetched_at: '2026-06-29T00:05:51.087975+00:00'
page_id: '1046836982'
product: rm
source: tdn-rm
title: Informe Rendimentos EFD-REINF (Autônomos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046836982
version: 8
---

# CONTEXTO

Os pagamentos realizados a **trabalhadores autônomos**, quando registrados diretamente no módulo Financeiro e declarados por meio do **eSocial**, não estão sendo contemplados automaticamente na geração do **Informe de Rendimentos** pelos módulos Fiscal e RH.

Essa situação ocorre especificamente neste fluxo operacional e não impacta os demais cenários de geração do Informe.

Até a disponibilização da solução definitiva em sistema, disponibilizamos abaixo um procedimento alternativo que permitirá o correto cumprimento da obrigação acessória, com base nos dados oficiais extraídos da base do sistema.

Siga as instruções a seguir para geração dos Informes de Rendimentos correspondentes.

---

# COMO GERAR O INFORME DE RENDIMENTOS

## ✅ Pré-requisito

Você deve ter baixado:

* A planilha modelo de Informe
* A consulta SQL para extração dos dados

Os dois artefatos estão disponíveis aqui mesmo nesta página!

false

---

# 🔹 PASSO 1 – Executar a consulta no sistema

1. Importe e execute a consulta SQL fornecida por dentro do RM. [Esta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004646072-Cross-Segmentos-Backoffice-RM-BI-Cria%C3%A7%C3%A3o-de-consultas-SQL) pode te ajudar com essa etapa.
2. Exporte o resultado para **Excel (.xlsx)**.
3. Copie todas as linhas retornadas (**SEM o cabeçalho**).

---

# 🔹 PASSO 2 – Inserir os dados na planilha

1. Abra a planilha do Informe.
2. Vá até a aba **BASE\_SQL**.
3. Cole os dados a partir da linha 2 (não altere os títulos das colunas).
4. Verifique se todas as linhas foram inseridas corretamente.

IMPORTANTE!

Não altere fórmulas nem exclua colunas.

---

# 🔹 PASSO 3 – Selecionar o Informe

1. Vá até a aba **TRATAMENTO**.
2. Na célula de seleção (B2), escolha o registro desejado.

A seleção é feita por:

```
CPF | Natureza do Rendimento
```

Cada opção corresponde a um Informe individual.

Importante!

O Total dos Rendimentos está sendo gerado pelo **Valor Baixado** (Coluna G). Porém, nos dados temos a informação do **Valor Original** também.

Logo, se você quiser gerar o Informe considerando Valor Original ao invés de Valor Baixado, basta alterar a fórmula da célula TRATAMENTO.B9 para:

=SEERRO(ÍNDICE(BASE\_SQL!$F:$F;CORRESP($A$2;BASE\_SQL!$J:$J;0));0)

---

# 🔹 PASSO 4 – Conferir os dados

1. Acesse a aba **INFORME**.
2. Verifique:

   * Nome da Fonte Pagadora
   * CNPJ
   * Nome do Beneficiário
   * CPF
   * Valores informados

Se estiver correto, prossiga para impressão.

---

# 🔹 PASSO 5 – Imprimir ou salvar em PDF

1. Na aba **INFORME**, insira na Linha 53 o Nome do Responsável pelas informações e a data. **Você só precisa fazer isso na primeira impressão!!**
2. Depois clique em:

   * Arquivo → Imprimir  
     ou
   * Arquivo → Exportar → Criar PDF
3. Salve ou imprima o documento.
4. Repita os processos 2 e 3 para os demais registros.

---

# 📌 Observações Importantes

* Cada registro da Consulta gera **um Informe distinto**.
* Caso o mesmo CPF possua mais de uma Natureza de Rendimento, será necessário gerar um informe para cada opção.
* **Não edite manualmente os valores na aba INFORME.**
* Sempre utilize os dados extraídos diretamente do sistema.

---
