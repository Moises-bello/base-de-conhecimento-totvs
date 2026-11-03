---
content_hash: bb826e32e0812aaa5efaa872b32587030003afc54aba567c4fcc433a4ba42fbc
fetched_at: '2026-06-29T00:08:43.951955+00:00'
page_id: '307835217'
product: rm
source: tdn-rm
title: FOPROTINAS01-1017 Exceções Novos Campos Exame Toxicológico CAGED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307835217
version: 96
---

# PREENCHIMENTO DOS NOVOS CAMPOS EM SITUAÇÕES DE EXCEÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | CAGED |
| **Situação/Requisito:** | Foi liberada instrução do MTE sobre o preenchimento dos novos campos referentes ao exame toxicológico nas seguintes situações de exceção: (1) o exame não ficou pronto a tempo do envio das informações ao CAGED; (2) o funcionário recusou-se a fazer o exame toxicológico demissional    <ftp://ftp.mtps.gov.br/pdet/arquivos/CAGED/Layout/6Excecoes.pdf> |
| **Solução/Implementação:** | Foi realizada tratativa para que o sistema identifique que trata-se de um preenchimento de dados referentes a uma das situações de exceção acima mencionadas quando o campo de código do laudo do exame for preenchido com os códigos 'PENDENTE000000000' ou 'RECUSA00000000000'. Assim, deve-se cadastrar normalmente os dados referentes ao exame marcado para o funcionário e, caso ocorra uma das situações de exceção mencionadas, basta inserir os códigos de laudo referentes às respectivas situações e o sistema levará para o CAGED os dados necessários para serem validados pelo MTE. Caso a situação de exceção seja solucionada, basta inserir o código de laudo correto e o sistema levará as informações reais cadastradas para o exame do funcionário.  É importante ressaltar a observação do MTE contida na instrução de preenchimento do CAGED em situações de exceção que foi liberada:  "OBS: O empregador terá o prazo 30 dias para informar a admissão ou desligamento do trabalhador com as informações do exame toxicológico como acerto. Após este prazo o empregador ficará sujeito à multa." |
| **Tickets relacionados:** | - |

divs
