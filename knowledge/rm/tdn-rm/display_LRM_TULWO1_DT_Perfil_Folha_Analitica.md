---
content_hash: 283f5b17fdbafcbc9d74b255c29c3105a50d0e5909f9da408be888054a5b36fb
fetched_at: '2026-06-29T00:06:29.555572+00:00'
page_id: '234612162'
product: rm
source: tdn-rm
title: TULWO1_DT_Perfil_Folha_Analitica
type: documentation
url: https://tdn.totvs.com/display/LRM/TULWO1_DT_Perfil_Folha_Analitica
version: 117
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Carregamento do Perfil para Folha Analítica* |
| **Situação/Requisito:** | Ao acessar os relatórios em DELPHI pelo Labore como Folha Analítica, Guia de INSS, só de clicar no ícone para abrir a rotina, é retornado a mensagem: "Temporary table resource limit".  SAÍDA DE CONTORNO:  Realizamos as configurações de adequação do blocksize do driver paradox para 32768 para solução da mensagem "temporary table resource limit".  Além disso, alteramos o caminho de criação do arquivo PDOXUSRS.Net para outros diretórios não solucionando o problema.  Uma vez que já havia sido identificado que o parâmetro BLOBS TO CACHE solucionava a questão, realizamos uma análise direcionada a possibilitar o ajuste dos BLOBS de forma que houvesse impacto a permissões de menu e outras rotinas.  Considerando uma margem de segurança, uma vez que este parâmetro não possui configuração fixa, realizamos o ajuste do mesmo para o valor de 960. |
| **Solução/Implementação:** | Foi identificado em que alguns pontos do carregamento do perfil era carregado muitos perfis já gravados. Então foi otimizado o carregamento do perfil de acordo com o tipo e registro do lookup de perfil selecionado. |
| **Conversores e Parâmetros:** | TULWO1 |
| **Chamados relacionados:** |  |
| **Requisito (ISSUE):** |  |

divs
