---
content_hash: b3303c300cfdf147bd1d9e2dfde7d04b35c09ab7a527ff361d5816b4c0ae6d22
fetched_at: '2026-06-29T00:08:49.686652+00:00'
page_id: '331855066'
product: rm
source: tdn-rm
title: RMFIS00010_Registro 0450
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00010_Registro+0450
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.x |
| **Ocorrência:** | Geração do Registro 0450 |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo**  O objetivo deste documento é oferecer orientações sobre a parametrização e geração do Registro 0450, no arquivo texto do SPED Fiscal/EFD Contribuições.    **Parametrização Necessária**  É necessário criar um campo Complementar para o Lançamento Fiscal(Movimento) tanto no **TOTVS Gestão Fiscal**, como no **TOTVS Gestão de Estoque, Compras e Faturamento**(caso opere como RM Nucleus). Uma vez preenchido o campo no RM Nucleus e escriturado, o mesmo é integrado com o sistema fiscal automaticamente.           Acesse: *Cadastros -> Campos Complementares -> Lançamentos Fiscais.***Nome da Coluna**: INFCOMPLDOCFISCAL   **Tipo**: Texto        **LANÇAMENTO FISCAL**    No RM Liber, acesse o documento fiscal: Tributação -> Situações Tributárias -> Informações Adicionais - Campos Complementares.        No RM Nucleus, acesse: *Cadastros -> Campos Complementares -> Movimentos****:* Nome da Coluna**: INFCOMPLDOCFISCAL   **Tipo**: Texto(Exatamente, o mesmo campo do sistema fiscal).    **MOVIMENTO**  No Movimento, o campo deverá ser preenchido em Informações Adicionais -> Campos complementares.        **Importante**: Todos os campos alfanuméricos terão tamanho máximo de 255 caracteres, exceto se houver indicação distinta, onde, neste caso, este tamanho distinto prevalecerá. |
| **Observações:** |  |
