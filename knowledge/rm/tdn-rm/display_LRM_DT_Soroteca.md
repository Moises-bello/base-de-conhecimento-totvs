---
content_hash: d7ec13bd7c65afd72bd7dcc44ae352b901c3245afcab04e4fb846e3cf58d3a1a
fetched_at: '2026-06-29T00:08:18.095416+00:00'
page_id: '262209813'
product: rm
source: tdn-rm
title: DT_Soroteca
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Soroteca
version: 4
---

# Soroteca

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Soroteca | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®/ Oracle® |
| **Tabelas Utilizadas:** | SZLOCARMAZENRACK, SZRACKAMOSTRA, SZSOROTECA, SZSOROTECALOG |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria consiste na criação do recurso de Soroteca para automação do gerenciamento e controle do armazenamento e descarte de amostras, fundamental para qualquer laboratório.

## Procedimento para Utilização

**Cadastrar Local de Armazenamento do Rack**

1. Acessar o **Menu Cadastros** / **Unidade de Diagnóstico** / **Local de Armazenamento do Rack**
2. Clique em **Incluir**.
3. Preencha o campo **Descrição**(obrigatório).
4. Clique em **Salvar** e/ou **OK**.

**Cadastrar Rack de Amostras**

1. Acesse o **Menu Cadastros** / **Unidade de Diagnóstico** / **Rack de Amostras.**
2. Utilize o botão **Incluir**.
3. Preencha os seguintes campos (obrigatórios):
   1. Nome do Rack.
   2. Número de Linhas.
   3. Linha inicia em.
   4. Número de Colunas.
   5. Coluna inicia em.
   6. Local de Armazenamento do Rack.
4. Clique em **Salvar** e/ou **OK**.

**Acesso a Soroteca**

1. Acesse o menu **Unidade de Diagnóstico** / **Soroteca.**

**Soroteca - Pesquisar Amostra**

1. Para pesquisar amostras é possível informar as seguintes informações, individualmente ou combinadas:
   1. Rack de Amostras.
   2. Número do Pedido de Exame (Ordem de Serviço).
   3. Nome ou Parte do Nome do Paciente.

Observação

* Quando o Rack de Amostras não for selecionado as amostras serão carregadas em coluna única independente se houverem amostras em racks distintos. Nestes casos, para identificar a localização da amostra
* As amostras vencidas serão exibidas com fundo vermelho para indicar o vencimento.

**Soroteca - Pesquisar Amostras informando apenas Rack de Amostras**

1. Acesse a funcionalidade Soroteca.
2. Preencha o campo **Rack** do **grupo Pesquisar.**
3. Selecione um **Rack de Amostras** / **Botão Pesquisar**.
4. O Rack selecionado carregará todas as amostras registradas.

**Soroteca - Pesquisar Amostras informando Rack de Amostras e Número do Pedido e/ou Nome do Paciente**

1. Acesse a funcionalidade Soroteca.
2. Seguir os seguintes passos:
   1. Preencha o campo **Rack** / Selecionar um **Rack de Amostras.**
   2. Preencha o campo **Pedido** e/ou **Paciente** / **Botão Pesquisar.**
      1. No campo **Paciente** é possível informar apenas parte do nome do paciente (ex.: "Maria").
   3. O Rack selecionado carregará **apenas** as amostras referentes ao **Paciente** e/ou **Pedido** informados no passo **2.b.**

**Soroteca - Rack de Amostras e Número do Pedido e/ou Nome do Paciente**

Observação

Quando o Rack de Amostras não é selecionado as amostras serão carregadas em coluna única independente se houverem amostras em racks distintos. Nestes casos, para identificar a localização da amostra.

1. Acesse a funcionalidade Soroteca.
2. Siga os seguintes passos:
   1. Preencha o campo **Pedido** e/ou **Paciente** / **Botão Pesquisar.**
      1. No campo **Paciente** é possível informar apenas parte do nome do paciente (ex.: "Maria").
   2. A Soroteca carregará em coluna única todas as amostras referentes ao **Paciente** e/ou **Pedido** informados no passo **2.a**
      1. Nestes casos a **localização** da amostra é exibida no grupo **Informações do****Tubo**, Campos Rack , Coluna e Linha.

**Soroteca - Incluir Amostras**

1. Acesse a funcionalidade Soroteca.
2. Preencha o campo **Rack** do **grupo Pesquisar**.
3. Selecione um **Rack de Amostras** / **Botão Pesquisar**
4. Marque a posição em que deseja incluir a amostra.
5. Preencha o campo **Validade** e **Cód**. **Barras** do grupo Incluir.
6. Clique em **Incluir.**
7. Após a inclusão a amostra utilizada será exibida na posição selecionada no passo anterior e o cursor de inclusão avançará uma posição para a direita.

**Soroteca - Excluir Amostras**

1. Acesse a funcionalidade Soroteca.
2. Preencha o campo Cod. Barras e Motivo do grupo excluir.
3. Clique em **Excluir**.  
   1. Caso a amostra excluída faça parte do Rack de Amostras atual, o rack será atualizado imediatamente após a exclusão.

**Soroteca - Logs das Soroteca**

1. Acesse a funcionalidade Soroteca.
2. Clique em **Logs** no grupo Excluir.
3. Visualizar os logs na tela **Soroteca Log**

**Soroteca - Histórico do Pedido de Exame**

1. Acesse o menu **Unidades Diagnóstico** / **Controle de Pedidos de Exames.**
2. Escolha um filtro para buscar um registro de Pedido de Exame.
3. Abra um registro de Pedido de Exame que contém ao menos uma amostra cadastrada na Soroteca.
4. Acesse a aba **Histórico de Controle** e **Visualizar** para encontrar a Ação Executada Amostras enviadas para a Soroteca.
