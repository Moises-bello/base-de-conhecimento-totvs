---
content_hash: 3c3f8a9b26aa5706a3fc8f6e7e255a9786d590fc8b8b84f873870bd16a597949
fetched_at: '2026-06-29T00:11:38.027293+00:00'
page_id: '781199594'
product: rm
source: tdn-rm
title: Novo Atendimento - Tipos de Cobertura
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Tipos+de+Cobertura
version: 2
---

Esta funcionalidade é responsável pelo cadastro dos ***Tipos de Coberturas*** que serão garantidas por um Empreendimento.

Os Tipos de Cobertura representam possíveis problemas que podem ocorrer na Subunidade (lote, loja, casa, apto. etc.), como por exemplo: Problemas de Alvenaria, Eletricidade, Hidráulica, etc.

Para acessar este cadastro, no contexto do módulo TOTVS Construção Gestão de Imóveis, acesse a aba de *Atendimento* e no agrupador de nome *Atendimento Revitalizado*, o menu ***Cadastro | Tipos de Cobertura***:

Ao abrir essa visão apresenta aos Tipos de Cobertura em forma de árvore hierárquica. Dessa forma, é possível de organizar e agrupar essas Coberturas de maneira mais adequada.

Ao inserir ou editar um Tipo de Cobertura são apresentados os campos abaixo:

Importante

Em relação à árvore hierárquica dos Tipos de Cobertura, caso se tenha associado um nível à garantia de uma venda, "*001.01 - Estrutural Nível 2*", por exemplo e posteriormente, se crie especificações dentro deste mesmo nível, "*001.01.01 - Estrutural Nível 3*", por exemplo, para que o sistema exiba estas garantias no momento de se [Gerar um Atendimento](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Gerar+Atendimento) para esta mesma venda, o parâmetro **[Permitir cadastrar atendimento de garantia sem Cobertura de Garantia vinculada a venda](https://tdn.totvs.com/pages/viewpage.action?pageId=435105270)**, deve estar marcado.

**Tipo de Cobertura:** Este campo não é editável e apresenta o Código de Identificação do Tipo de Cobertura criado. Sendo que no momento de inclusão de um novo registro, o mesmo apresenta o valor padrão -1, que será substituído posteriormente, pelo Código de Identificação gerado automaticamente pelo sistema ao salvar este registro;

**Código Hierárquico:** Este campo apresenta o Código de Hierárquico do Tipo de Cobertura que é criado, de acordo com a [Máscara do Código da Cobertura](https://tdn.totvs.com/pages/viewpage.action?pageId=435105270), definida no *Etapa 2*, dos *Parâmetros do TCGI*.

No momento de inclusão de um novo registro, o Usuário deverá digitar o código em formato numérico de acordo com a máscara e a hierarquia parametrizada;

**Grupo de Coberturas:** Este campo não é editável, ele é preenchido automaticamente pelo sistema quando a Cobertura visualizada em outras Coberturas cadastradas na hierarquia abaixo dela (estilo subcobertura ou cobertura derivada);

**Descrição:** Campo para descrever o Tipo de Cobertura que será cadastrado;

**Tipo de Início de Vigência:** Campo que define qual data será considerada para o Início da Vigência da Cobertura cadastrada. Podem ser escolhidas uma das datas a seguir:

* Data da venda
* Data da entrega do empreendimento
* Data do habite-se
* Data da entrega das chaves
* Data de assinatura

**Período de Vigência (meses):** Esse campo define a duração (em meses) da cobertura.  
*Observação:* O Tipo de Início de Vigência e o Período da Vigência são valores default, mas estas opções podem ser modificados dentro dos Modelos, no Empreendimento, nas Subunidades ou nas Vendas, conforme a necessidade de cada uma destas Entidades.

Informações Complementares

---
