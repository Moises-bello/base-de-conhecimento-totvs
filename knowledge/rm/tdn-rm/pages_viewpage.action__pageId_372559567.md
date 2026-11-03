---
content_hash: cb23d0eed279211596ca28045da5403364ca0763ba5b6c77b6688b78077f46f6
fetched_at: '2026-06-29T00:09:01.500979+00:00'
page_id: '372559567'
product: rm
source: tdn-rm
title: 1461899 FISCAL01-1794 DT Alteração do registro 0450 do SPED Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372559567
version: 1
---

# Remoção de caracteres em branco do fim do campo txt

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Rotina estadual SPED Fiscal |
| **Situação/Requisito:** | Ao validar o Sped Fiscal foi apresentada a seguinte mensagem: Campo não pode conter espaços em branco no início nem no final. è Registro 0450 – Campo txt. |
| **Solução/Implementação:** | Remoção de caracteres em branco ao truncar o campo caso extrapole o tamanho máximo do campo que é de 255 caracteres. |
