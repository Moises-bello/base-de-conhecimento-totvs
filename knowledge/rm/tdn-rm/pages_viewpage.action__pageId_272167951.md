---
content_hash: 59f4c47ffeb8ac9081f079a61e33565309f83442eca0405eedb4767850b4fa6f
fetched_at: '2026-06-29T00:08:30.062773+00:00'
page_id: '272167951'
product: rm
source: tdn-rm
title: RMFIS00001_Geração e consistências da rotina Apuração GIA - ST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272167951
version: 6
---

# Assunto:

O objetivo deste documento é de orientação ao processo atual de geração da rotina fiscal Estadual GIA ST (Guia Nacional de Informação e Apuração do ICMS Substituição Tributária.

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.15 |
| **Ocorrência:** | Geração da Rotina |
| **Ambiente:** |  |
| **Passo a passo:** | **Regras Gerais:**   * A geração da rotina é realizada pelo executável do aplicativo RMLiber, através do menu Rotinas Legais/Rotinas Estaduais/Apuração de GIA – ST/Apuração GIA ST. * O arquivo txt gerado pelo sistema é apenas de consulta para digitação dos dados no programa de Digitação da GIAST.     **Parametrização Necessária:**  Na tela de geração da rotina, o campo "Arquivo Texto", virá com o nome default GIAST.txt, mas o campo é editável e permite que seja informado o nome do arquivo Texto a ser gerado pelo sistema.   * Campo Filial: Permite que seja informado a Filial a qual se deseja gerar o arquivo. * Campo Estado: Informe o estado para geração do arquivo. * Campo Referência: Informe o período a que se refere a GIA ST. Este período já deverá estar cadastrado no Períodos de Apuração. * Flag GIA Substituição:  Marque essa opção caso a GIA ST gerada for para substituir alguma que já foi gerada. * Flag Gerar Dados Diferencial de Alíquota e campo Referência DIFAL: Ao marcar o checkbox "Gerar Dados Diferencial de Alíquota", o campo "Referência DIFAL" deverá ser habilitado para seleção do período de apuração do ICMS. Ao selecionar um período de apuração de ICMS, os dados a serem inseridos na seção para dados de DIFAL e FECP serão carregados a partir da aba "Valores Diferencial de Alíquota" (tabela DPERIODODIFAL) de seu cadastro. * Imagem da tela Apuração da GIA ST:   **Consistências:**  As consistências do sistema são com base nos lançamentos fiscais (entrada/saída), escriturados no RMLiber.   * Devem existir os períodos de apuração dos tributos tipo ICMS e ICMSST. * Para os lançamentos com diferencial de alíquota e FCP (Fundo de Combate à Pobreza), serão consistidos os lançamentos fiscais de saída, com diferencial de alíquota, valores FCP, de acordo com as regras da EC 87/15. * Link apoio EC 87/15:EMENDA CONSTITUCIONAL Nº 87, DE 16 DE ABRIL DE 2015 * Antes de gerar a rotina, encerre os períodos de apuração e confira os valores apurados.   **Relatório exemplo:**  Imagem exemplo do arquivo gerado pelo sistema.  **OBS:** Os dados relacionados ao contribuinte e declarante, são com base na parametrização definida no cadastro da Filial, na opção de Anexos – Dados Fiscais. |
| **Observações:** | * As imagens exibidas nesse documento são meramente ilustrativas para a descrição e entendimento do processo. * O processo atende desde a versão 11.52. * Os campos "Gerar Dados Diferencial de Alíquota" e campo "Referência DIFAL", foram criados em melhoria a partir da versão 12.1.13. |
