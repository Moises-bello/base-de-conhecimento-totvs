---
article_id: 39640805635991
category: Anuais
content_hash: 1e6a7daee95f351240fbd5dcd0d9d97249abc4b064ee1fd8cc9abffaac72263f
fetched_at: '2026-06-28T22:46:50.972983+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP-Emissão da DIRF para Conferência e Informe de Rendimentos
type: support-article
updated_at: '2026-04-09T21:18:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39640805635991-RH-RM-FOP-Emiss%C3%A3o-da-DIRF-para-Confer%C3%AAncia-e-Informe-de-Rendimentos
---

## time.png  Tempo aproximado para leitura:**00:02:00 min**

**Dúvida** Como realizar a parametrização e emissão da DIRF para conferência e do Informe de Rendimentos para anos-base posteriores a 2024.

**Ambiente**

TOTVS RH (Linha RM) - Folha de Pagamento - A partir dos patches:

12.1.2502.285, 12.1.2506.251, 12.1.2510.174, 12.1.2602.100 e superiores.

**Solução** O sistema permite a geração da DIRF em diferentes formatos (Arquivo, Conferência ou Informe). Para anos-base como 2025 (DIRF 2026), o processo centraliza-se na conferência e não gera arquivo dos valores tributáveis, isentos e deduções baseadas em códigos de cálculo específicos.

**Passos**

1. **Acesso ao Menu:**

   * Navegue em Anuais | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos.
   * Selecione o **Perfil de Parâmetros** e, na tela seguinte, escolha a opção **DIRF para Conferência** no topo da janela.
2. **Opções de Geração do Informe:**

   * **Lançar valores para o Gerador de Relatórios:** Utilize esta opção para gravar os dados na tabela **PDIRF**, permitindo a visualização no **RM Portal**.
   * **Deletar Ano de Referência:** Marque este campo para limpar registros anteriores e evitar duplicidade ao regerar as informações.
   * **Enviar por e-mail:** Caso deseje enviar o comprovante em PDF diretamente ao funcionário, preencha o e-mail do remetente e marque o parâmetro **Comprovante de Rendimentos**.
3. **Conferência de Valores (Composição dos Campos):**

   * **Rendimentos Tributáveis (Campo 3):** Soma eventos com incidência de IRRF, deduzindo estornos, exceto os códigos de cálculo 13, 113 e 57.
   * **Previdência Oficial:** Calculada através da fórmula (89+90+137+132+85+179)-92$.
   * **Pensão Alimentícia:** Composta pelos códigos (13+113+53+195+197+319+326+320+386)-(199+201+327)$.
   * **13º Salário Líquido (Campo 5):** Apura o valor líquido subtraindo da base as deduções de INSS, dependentes e previdência privada.
4. **Informações Complementares e Saúde:**

   * O sistema detalha na **Linha 07** os valores de assistência médica (titular e dependentes) e previdência privada.
   * Os dados de saúde são extraídos da aba **Operadora de Assistência à Saúde** no cadastro do módulo.

Saiba mais: [FOP\_0002\_Emissão DIRF/Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682#1-2)
