---
content_hash: 02bc5d64cb8ec6cedf459e8c65302f5da46519e25adc653905005037a2790d25
fetched_at: '2026-06-29T00:11:45.091402+00:00'
page_id: '819495446'
product: rm
source: tdn-rm
title: Índice de Acompanhamento - TCOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819495446
version: 12
---

**Índice de Acompanhamento**  
Permite cadastrar os valores do índice que será utilizado para aferir a qualidade de um objeto de manutenção através de medição periódica. São estabelecidos no momento da criação do índice, valores  
mínimos e máximos aceitáveis de qualidade. Baseado neste intervalo, o sistema classifica o objeto da seguinte maneira: valor do índice abaixo do mínimo, valor do índice dentro da faixa, valor do índice acima do máximo. Os valores mínimos e máximos escolhidos para os índices de acompanhamento podem variar dentro do conjunto dos números racionais (-4,124; -3; 0; 9; 17,865).

Para trabalhar com apropriação direta de produto, na tela de cadastro de índice de acompanhamento marque o parâmetro “Apropriação Direta de Produto” e depois na tela de cadastro de Objeto de  
Manutenção / Anexo – Produto do Objeto de Manutenção cadastre o produto a ser apropriado. Informe a quantidade a ser apropriada, a data de inicialização e o consumo médio do produto para o Objeto de Manutenção. Após fazer o cadastro como mostra a figura abaixo, ao acessar o menu Operações / Apropriação Direta de Produto(s) informar o identificador do Objeto de Manutenção o produto ficará visível para fazer a apropriação. Veja mais detalhes no tópico Apropriação Direta e Medição de Consumo.

**Telemetria**

Foi adicionada uma nova aba no cadastro de Índice de Acompanhamento voltada para quando estiver integrado com .

Nessa aba, é possível selecionar um índice já existente para acompanhar um item específico desejado, para o determinado objeto cadastrado.

Essa funcionalidade permite trazer mais contexto e rastreabilidade para as informações enviadas pelo sistema, facilitando o monitoramento em tempo real de dados relevantes.

Para utilizar, basta acessar a aba Telemetria, escolher o índice que representa o item a ser acompanhado e salvar.

Vale lembrar que esse acompanhamento só será possível se o usuário estiver **autenticado e se a funcionalidade estiver devidamente parametrizada** na aba de **Integrações dos Parâmetros de Manutenção.**

Para mais detalhes acesse a documentação de integração com .

Ao clicar para abrir  irá ser apresentado uma lista com todos os índices para acompanhamentos cadastrados.

Caso saiba o código de algum dos índices, ele poderá ser digitado diretamente no campo, sem a necessidade de abertura da lista com todos os índices.
