---
content_hash: 086e82ea89e4f99d7d53477feaf01c38b4f88e7db20b2d0b59ddc4fe99acd3bc
fetched_at: '2026-06-29T00:08:51.064822+00:00'
page_id: '336403790'
product: rm
source: tdn-rm
title: RMFIS00012_Registro C176
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00012_Registro+C176
version: 15
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X. |
| **Ocorrência:** | Parametrização do Registro C176. |
| **Ambiente:** |  |
| **Passo a passo:** | Este registro é de uso exclusivo para contribuintes para os quais a legislação estadual utiliza o método de ressarcimento pelo valor da última entrada e exige a emissão do documento fiscal na solicitação de ressarcimento em operações com substituição tributária.  Vide manual da rotina:  **REGISTRO C176: RESSARCIMENTO DE ICMS EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55)**  Este registro deve ser informado quando da escrituração de documento fiscal, que acoberte operação que represente desfazimento de substituição tributária realizada em operações anteriores.  O documento informado neste registro deverá ser diferente do documento informado no registro pai (C100), pois é o documento referente à(s) última(s) aquisição(ões) da mercadoria e à retenção do imposto.  **Abaixo contém as orientações para correta geração do registro C176 no sistema para o SPED Fiscal.**  1. O sistema considera lançamentos de saídas, mercadorias sujeitas ao regime de substituição tributária;  2. O tipo de documento informado deverá conter o "Código do Modelo de Documento" como "01" ou "55";    3. Natureza de Operação (CFOP) deverá ser do grupo: 6.4;      5. É necessário vincular o documento de entrada no item do lançamento/ aba de informações adicionais - sub aba referências: (Neste caso a aba só ficará disponíveis para naturezas fiscais do grupo 6.4)      A associação demonstrada acima, também pode ser realizada de forma automática. [Clique aqui](https://www.google.com/url?q=https://tdn.totvs.com/pages/releaseview.action?pageId%3D438273534&sa=D&source=hangouts&ust=1567257181196000&usg=AFQjCNGeIASNj1QjsaD0DZsX6H_xwLQ1lQ) para ter acesso a documentação.  Após seguir os passos acima, o sistema irá levar corretamente o registro C176 para o SPED Fiscal. |
| **Observações:** | [Para mais orientações](http://tdn.totvs.com/display/public/LRM/ER_MEDU-31_Sped_Fiscal_Registro_C176):  **C[onsistências técnicas para geração do registro](http://tdn.totvs.com/display/public/LRM/ER_MEDU-31_Sped_Fiscal_Registro_C176)** |
