---
content_hash: 727af334a35baa270e0f83ce19168cbe284221f75153fb90586c2ddde38aad73
fetched_at: '2026-06-29T00:09:28.635496+00:00'
page_id: '423938730'
product: rm
source: tdn-rm
title: Demonstrações Contábeis | Gerar Demonstrações Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938730
version: 6
---

O processo de Gerar Demonstrações contábeis possibilita a exportação ou visualização da Estrutura (Layout) em forma de relatório.

O acesso a esse recurso é possível de duas formas:

1. Gerado através do menu de Processos | Gerar Demonstrações Contábeis.
2. Menu [Escrituração Contábil] ->[Apuração → Demonstração Contábil] ->[Opção →"Gerar Demonstrações Contábeis" ].

São informações **obrigatórias** o Layout da Demonstração, assim como a Data Início e Data Final de emissão dos dados contábeis. De forma opcional, conforme a necessidade de informações a serem emitidas, pode-se utilizar um Filtro Genérico e utilizar as opções de impressão "Gerar relatório conforme será visualizado no SPED", "Gerar prévia do relatório em uma visão de dados (poderá ser exportada para Excel)" e ainda "Não mostrar sinal para os valores processados".

As opções em Tipo de Valor dão flexibilidade na escolha da moeda a ser demonstrada no relatório, sendo o Valor Principal ($) a moeda padrão da Coligada Corrente, ao optar por Cotação em Outra Moeda será disponibilizado a lista de Moedas parametrizadas para a Coligada corrente. Independente da moeda colocada como principal nas demais coligadas, o sistema irá apresentar o valor referente a moeda escolhida.

**Atenção:** Caso não exista valor calculado para a moeda selecionada, o valor gerado será zero.

**Observação:** Na visualização da prévia do relatório, pode ser que as colunas não correspondam a ordem configurada na estrutura da demonstração.   
                     Isso acontece porque a tela de prévia guarda as preferências do usuário, ou seja, caso o usuário altere a ordem das colunas manualmente ou esconda uma coluna por exemplo, essa configuração será guardada nas preferências e na próxima vez que a tela de prévia for aberta, esta irá respeitar o que foi configurado anteriormente.

Os campos Título Relatório, Subtítulo Relatório, Subtítulo Complementar, Titulo Coluna Código do Fato Contábil, Titulo coluna Fato Contábil, Imprimir código do Fato Contábil e Indentar descrição do fato Contábil conforme a máscara do código, deverão ser informados conforme a necessidade do cliente.

As configurações de impressão realizadas poderão ser Salvas, ao clicar sobre o campo "Preferências (Configurações de Tela) | Salvar" será possível Salvar a estrutura de impressão, nomeá-la, para sua utilização posterior. Sendo que para utilizá-la posteriormente basta clicar em "Preferências (Configurações de Tela) | Abrir/Excluir (selecionar a estrutura salva anteriormente) | OK".

Relatório de Parametrização:

Gerado através do menu de Processos | Relatório de Parametrização, possibilita a visão descrita de cada célula do relatório, bem como os dados de Origem do Valor e Contas parametrizados nas células. É utilizado para a conferência de parametrização do relatório.
