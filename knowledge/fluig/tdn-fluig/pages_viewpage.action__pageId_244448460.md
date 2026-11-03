---
content_hash: adf77284a5bde86602ea6bcd281222e7cf80a28e96e70a7a164d2bf9ed54a0bb
fetched_at: '2026-06-28T21:35:23.239480+00:00'
page_id: '244448460'
product: fluig
source: tdn-fluig
title: Nomenclatura e Estrutura de Formulários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244448460
version: 8
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é apresentar a estrutura dos formulários, bem como boas práticas de nomenclatura e dicas para o desenvolvimento.

## Nomenclatura

### Código do Processo

Para convencionar os processos que serão criados, os códigos devem seguir o seguinte padrão: *(area) \_ (ação)*

Exemplo

### Serviços

Para convencionar os serviços que serão incluídos, os códigos devem seguir o seguinte padrão: *(sistema) \_ (processo)*

Exemplo

### Código do Dataset

Para convencionar os datasets que serão criados, os códigos devem seguir o seguinte padrão: *(sistema) \_ (transação) \_ (item/artefato)*

Exemplo

### Mecanismo

Para convencionar os mecanismos que serão criados, os códigos devem seguir o seguinte padrão: *(sistema) \_ (processo)*

Exemplo

### Campos no Formulário e Variáveis

Devemos manter os seguintes prefixos de campos do formulário e para variáveis.

| Prefixo | Tipo | Exemplo |
| --- | --- | --- |
| vl | Valor | vl\_total , vl\_telefone |
| nm | Nome | nm\_cliente , nm\_fornecedor |
| dt | Data | dt\_emissao , dt\_faturamento |
| lb | Booleano | lb\_temfrete , lb\_emiteboleto |
| ds | Textarea | ds\_comentarios , ds\_observacoes |
| cb | Combo box | cb\_estado , cb\_cidade |

Atenção!

Não é possível alterar o tipo de um campo anteriormente criado no formulário. Esta alteração não será refletida no banco de dados.

Como paliativo, é possível alterar o nome do campo de formulário. Desta forma ele será registrado no banco de dados como um novo campo.

## Estrutura

---

Para entendimento do modelo, o formulário é dividido em três partes sendo o Cabeçalho, Conteúdo e Rodapé.

Os campos de formulário são constituídos por *labels* e campos de edição. Esse *label* deve ser posicionado acima do campo de forma a garantir a [internacionalização](http://tdn.totvs.com/pages/viewpage.action?pageId=185738869) (i18n) e localização (L10n) do produto.

É possível agrupar grandes quantidades de informações utilizando agrupadores por localização.

### Cabeçalho

O cabeçalho se encontra na parte superior do formulário e dever ser utilizado para apresentar o título explicativo sobre a coleção de dados. Neste local também, alinhado à direita, pode ser inserido a logomarca do cliente. O tamanho sugerido é de 150px x 50px.

### Conteúdo

A área de conteúdo se encontra na parte intermediária do formulário, entre o cabeçalho e rodapé, e dever ser utilizado para apresentar a coleção de dados.

### Rodapé

O rodapé se encontra na parte inferior do formulário, e dever ser utilizado para apresentar as ações relacionadas e disponíveis para a coleção de dados quando necessário.

### Elementos

Conforme a imagem abaixo, podemos verificar os elementos essenciais. O título deve estar alinhado à esquerda e sempre que possível ser correspondente à coleção de dados. Os dados, de preferência, devem estar agrupados*, labels* sempre acima dos *InputText* e botões com ações localizados no rodapé alinhados à direita.

### Dimensões

Os formulários devem ter seu tamanho adaptável a tela, não deve ter tamanho fixo.

## Dicas Práticas

---

* Monte a ordem dos campos no formulário respeitando as regras do negócio relacionadas àquele conteúdo.

* Utilize \* para marcar os campos obrigatórios;

* Evite campos desnecessários;

* Sempre que possível, na entrada de dados, utilize máscaras (CPF, RG, CNPJ, DATA, HORÁRIO, MOEDA) para impedir letras em um campo numérico;

* Defina a largura dos campos no tamanho dos seus caracteres no banco;

* Se for necessário, limite o máximo de caracteres possíveis (*maxlength*);

* Use *Dataset*s para carregar dados em um *ComboBox*;

* Mantenha os formulários com *Labels* em cima e campos abaixo;

* Zoom e *ComboBox* devem ser utilizados no lugar de campos vazios, o usuário não deve precisar memorizar dados desnecessários;

* Opções não disponíveis ficam desabilitadas. Campos somente leitura devem aparecer como *label*, pois facilita a leitura e a legibilidade da tela;

* Itens de formulário devem possuir validações que não deixam o usuário trocar de campo sem corrigir dados inconsistentes. Esse item garante o critério ergonômico de prevenção de erros;

* Os formulários devem permitir a navegação através do teclado, de forma que a tecla ‘*TAB’* direcione o foco para o próximo campo e ‘*SHIFT + TAB*’ para o campo anterior. *Nesse caso, deve-se definir a ordem dos componentes.* Quando existirem formulários múltiplos (várias abas), o usuário será redirecionado para a próxima sessão do formulário ao chegar ao fim da página;

* Para o HTML, prefira utilizar o HTML Encode das letras com acentuação. Exemplo: ***é** → **&eacute***. [Obtenha mais informações](http://www.w3schools.com/tags/ref_entities.asp).
