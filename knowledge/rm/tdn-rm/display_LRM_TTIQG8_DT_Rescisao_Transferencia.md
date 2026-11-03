---
content_hash: 6efbe728e137114e7f01d2bfd786ddce03bd9f2759c1fe9e448170eb47918bae
fetched_at: '2026-06-29T00:06:13.083337+00:00'
page_id: '208339157'
product: rm
source: tdn-rm
title: TTIQG8_DT_Rescisao_Transferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIQG8_DT_Rescisao_Transferencia
version: 2
---

# Rescisão por transferência

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Transferência* |
| **Situação/Requisito:** | Ao realizar a demissão do funcionário no Tipo 5 ou 6 (Transferência) e clicar em Salvar, ao fechar o cadastro da rescisão, o funcionário continua na situação Ativo porém preenche o campo Data de demissão. |
| **Solução/Implementação:** | Conforme alinhado, a funcionalidade de transferência foi reformulada na versão 12. Quando o processo de rescisão do tipo 5 ou 6 não é concluído o funcionário continua na Situação de ativo (“A”) , evitando assim, algumas inconsistências:     * Cálculo de folha:  Para funcionários em processo de transferência não concluído, o sistema calculava verbas rescisórias, se baseando no status "Demitido" dos mesmos. * Liberação de competência: Após a liberação da competência não era possível continuar o processo de transferência do funcionário.     Na versão 12, além do funcionário continuar na situação de ativo (“A”), será preenchido o campo “Data de Demissão”, possibilitando a utilização dessa referência como filtro de funcionários em processo de transferência.   As rescisões do tipo 5 ou 6 são tratadas de forma diversificada pois o processo de transferência cria uma nova chapa em outra Filial ou Coligada, alterando a situação do funcionário para demitido (“D”) apenas quando já existir um novo registro como Ativo. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTIQG8 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
