---
content_hash: b7e4adce9a77c2bbd235831ed2225473b028de16a95989648faa24dd615e5e3c
fetched_at: '2026-06-29T00:10:08.875310+00:00'
page_id: '452719599'
product: rm
source: tdn-rm
title: Parametrização Integração Totvs Gestão de Estoque, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719599
version: 2
---

**Parametrização Integração Totvs Gestão de Estoque, Compras e Faturamento** 

Quando integrado com o Totvs Gestão de Estoque, Compras e Faturamento, é de extrema importância que este esteja totalmente parametrizado e seja controlado continuamente.  
Para que a Integração tenha sucesso será necessário observar:

**Locais de estoque cadastrados**

**Criar quatro tipos de movimentos**

Entrada de EPI's, Empréstimos de EPI's, Devolução de EPI's e Baixa de EPI's. Recomenda-se não utilizar o mesmo local de estoque dos demais produtos cadastrados no Totvs Gestão de Estoque, Compras e Faturamento, para facilitar o controle e gerenciamento do estoque dos EPI's.

**Parametrizando os Movimentos**

Será necessária a parametrização de quatro Tipos de Movimentos:

1.2.xx – para Entrada de EPI's;  
3.1.xx – para Transferência de EPI's;

1.2.xx – Para Devoluções de EPI's;

2.2.xx – Para Baixas de EPI's;

2.2.xx – Para Empréstimos de EPI's;

1.2.xx – para Devolução (descarte) EPI's

**Movimento – Entrada de EPI's**

O Movimento de entrada de EPI's controlará as aquisições de EPI's. As seguintes parametrizações serão necessárias:

- **Destinatário:** Empresa;

- **Edição de Local de Destino:** Informar local de estoque previamente cadastrado.

- **Edição de Preço:** Edita; - **Saldo atual:** Aumenta;

- **Recursos Humanos:**Compras.

**Movimento – Transferência de EPI's**

O movimento de transferência para realizar o controle de EPI'S(EX transferência entre centro de custos.). As seguintes parametrizações serão necessárias:

- **Tipo de Itens:**Ambos;

- **Numeração:** Mostra;

- **Emitente:** Empresa;

- **Destinatário:** Empresa;

- **Edição de Local de Destino:** Não Edita;

- **Edição de Preço:** Edita;

- **Saldo atual:** Diminui;

- **Unidade de Medida Padrão:** Unidade de Controle;

- **Recursos Humanos:** Transferência.

**Movimento – Devolução de EPI's**

O movimento para devolução de EPI's controla a saída dos EPI's. As seguintes parametrizações serão necessárias:

- **Tipo de Itens:** Produtos;

- **Numeração:** Mostra;

- **Emitente:** Empresa;

- **Edição de Local de Origem:** Informar local de estoque previamente cadastrado onde se encontra os EPI's;

- **Destinatário:** Cliente;

- **Edição de Local de Destino:** Informar local de estoque previamente cadastrado onde estão sendo devolvidos os EPI's;

- **Edição de Preço:** Diminui;

 **Saldo atual:** Aumenta;

- **Recursos Humanos:** Devolução.

**Movimento – Baixa de EPI's**

O movimento para baixa de EPI's controla a saída dos EPI's. As seguintes parametrizações serão necessárias: 

- **Tipo de Itens:** Produtos;

- **Numeração:** Mostra;

- **Emitente:** Empresa;

- **Edição de Local de Origem:** Informar local de estoque previamente cadastrado onde se encontra os EPI's;

- **Destinatário:** Empresa;

- **Edição de Local de Destino:** Informar local de estoque previamente cadastrado onde estão sendo devolvidos os EPI's;

- **Edição de Preço:**  Edita;

- **Saldo atual:** Diminui;

- **Recursos Humanos:** Baixa EPI.

**Movimento – Empréstimo de EPI's**

O movimento para empréstimo de EPI's controla os empréstimos de EPI's. As seguintes parametrizações serão necessárias: 

- **Tipo de Itens:** Produtos;

- **Numeração:**Mostra;

- **Emitente:** Empresa;

- **Edição de Local de Origem:**Informar local de estoque previamente cadastrado onde se encontra os EPI's;

- **Destinatário:** Empresa;

- **Edição de Local de Destino:** Informar local de estoque previamente cadastrado onde estão sendo emprestados os EPI's;

- **Edição de Preço:** Não Edita;

- **Saldo atual:** Diminui;

- **Unidade de Medida Padrão:** Unidade de Controle;

- **Recursos Humanos:** Empréstimo.

**Movimento – Baixa de EPI's (devolução)**

O movimento para Baixa de EPI's controla os materiais que não serão mais utilizados, mas que entraram no estoque. (EX: Devolução de material descartável, desgastado, estragado, etc.)   As seguintes parametrizações serão necessárias:

- **Tipo de Itens:**Produtos;

- **Numeração:** Mostra;

- **Emitente:** Empresa;

- **Edição de Local de Origem:** Informar local de estoque previamente cadastrado onde se encontra os EPI's;

- **Destinatário:** Empresa;

- **Edição de Local de Destino:** Não Edita;

- **Edição de Preço:** Edita;

- **Saldo atual:** Diminui;

- **Unidade de Medida Padrão:** Unidade de Controle;

- **Recursos Humanos:** Baixa de EPI.  

Para informações mais detalhadas, favor consultar o Help do Totvs Gestão de Estoque, Compras e Faturamento.
