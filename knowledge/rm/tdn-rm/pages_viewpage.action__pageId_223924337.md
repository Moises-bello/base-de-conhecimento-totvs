---
content_hash: df6720a5947774c78c054fa4e63ab3119fc251a1ca18bcd75f001890ae6c46f4
fetched_at: '2026-06-29T00:06:22.632150+00:00'
page_id: '223924337'
product: rm
source: tdn-rm
title: RMFIS00003_Geração do Registro 1700
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223924337
version: 126
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 11.82.42.x |
| **Ocorrência:** | Geração do registro 1700 - Documentos Fiscais Utilizados |
| **Ambiente:** |  |
| **Passo a passo:** | De acordo com o Guia Prático do Sped Fiscal: “devem ser informados os dispositivos autorizados e utilizados na emissão de documentos fiscais no período da EFD-ICMS/IPI. A obrigatoriedade deste registro deve ser verificada junto a cada uma das unidades federativas.”    Para geração do registro 1700 o sistema irá verificar as informações da AIDF (Autorização para Impressão de Documento Fiscal) vinculada ao lançamento fiscal.  Para verificar as AIDFs cadastradas no sistema acesse: TOTVS Gestão Fiscal | Cadastros | Específicos – Mais | AIDF      Verifique também se o Item da AIDF está cadastrado corretamente.  TOTVS Gestão Fiscal | Cadastros | Específicos – Mais | AIDF | Selecione a AIDF | Anexos | Itens AIDF      A AIDF será vinculada ao lançamento fiscal Aba Cabeçalho | Campo Número AIDF.    Ao salvar o lançamento fiscal é possível que seja apresentado a seguinte mensagem:    Para que isso não ocorra é necessário que o Item do cadastro da AIDF seja compatível com o lançamento fiscal.    **Geração da rotina.**  Marque na tela de geração da rotina, aba Personalização, a opção “Gerar registro: 1700”.  OBS: Caso o parâmetro esteja desmarcado o sistema **não** gerará o registro.  Para gerar a rotina acesse:  - TOTVS Gestão Fiscal | Obrigações Acessórias | Sped Fiscal      Caso o lançamento esteja sem o AIDF vinculado será apresentado a seguinte mensagem no log de geração da rotina:    Para correção da mensagem basta acessar o lançamento informado e inserir o AIDF. Lembrando que o lançamento fiscal sem AIDF não será apresentado no registro 1700.    **Trecho do arquivo Gerado.**      **Registro x Campos:**  **Campo 2 -** **COD\_DISP:** Será preenchido de acordo com o campo “Tipo do Dispositivo de Segurança” informado no cadastro do AIDF.  **Campo 3 - COD\_MOD:** Será informado de acordo com o Código Modelo de Documento informado na Dados Adicionais do Tipo de Documento vinculado ao lançamento fiscal e Itens do AIDF.  **Campo 4 e 5 – SER e SUB:** Serão preenchidos conforme os campos Série e Subsérie do lançamento fiscal.  **Campo 6 e 7 – NUM\_DOC\_INI e NUM\_DOC\_FIN**: Será informado o Número do Documento Inicial e Final do lançamento fiscal.  **Campo 8 – NUM\_AUT:** Será preenchido de acordo com o campo “Número da Autorização” informado no cadastro da AIDF. |
| **Observações:** |  |

divs
