---
content_hash: 7c24fc2c362985e11a540a22f7b15c003e799e6550f47475b2bb8ef18d411019
fetched_at: '2026-06-29T00:08:43.080988+00:00'
page_id: '301187913'
product: rm
source: tdn-rm
title: RMFIS00006_Configuração da Action FinCFODataBR Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301187913
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.x |
| **Ocorrência:** | Aumentar o número máximo de registros na visão de Cliente/Fornecedor |
| **Ambiente:** |  |
| **Passo a passo:** | Ao realizar um filtro genérico que traga TODOS os Clientes/Fornecedores cadastrados no sistema, pode ser apresentado a seguinte mensagem de alerta:          A quantidade de registros que seriam apresentados como resultado do filtro é superior a configurada na *Action* do sistema. Para aumentar este limite, configure: Acesse o módulo de Serviços Globais → Serviços – Servidores de Aplicação        Execute um filtro de seleção e insira um novo registro e busque pelo ID Server **FinCFODataBR**.      Informe o número máximo de registros, como destacado nas imagens. |
| **Observações:** | Quanto maior for o número de registros configurados, maior será o tempo de resposta do sistema. Recomendamos o máximo de 1000 registros. |
