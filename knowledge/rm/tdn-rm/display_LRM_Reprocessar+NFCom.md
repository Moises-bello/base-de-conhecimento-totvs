---
content_hash: 6221b5572de0fa4b700d71c2d005b4f28dbd79cab3ac7693b5afe94805a1c490
fetched_at: '2026-06-29T00:12:14.627973+00:00'
page_id: '969125857'
product: rm
source: tdn-rm
title: Reprocessar NFCom
type: documentation
url: https://tdn.totvs.com/display/LRM/Reprocessar+NFCom
version: 32
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo "Reprocessar NFCom", disponível no módulo *TOTVS Gestão de Estoque, Compras e Faturamento*, tem como objetivo corrigir o XML do documento fiscal que contenha erro. Para isso, o usuário deve selecionar a(s) nota(s) e executar o processo "Reprocessar NFCom para que o xml seja atualizado conforme fluxo abaixo.

---

# 2. Fluxo do Processo

Abaixo é detalhado o fluxo do processo de Reprocessar NFCom, ao clicar em algumas etapas o processo será detalhado.

falseReprocessar XMLfalseautohiddentrue109111

60%#0022331dashedDetalhes

---

# 3. Configurações iniciais

Para acessar o menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)* e Reprocessar a Nota, é necessário fornecer a permissão da **Nota Fiscal de Comunicação Eletrônica (NFCom),** conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom), [04.02.01.07.08] Gerar NFCom** e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - Perfis

---

# 4. Execução do Processo

Reprocessar NFCom:

ExecuçãoReprocessar NFCom

Para executar o processo basta selecionar as notas com status "Inconsistente", "Rejeitada" ou "Editada" e acionar o processo através do menu ***Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos | Reprocessar NFCom***.

Reprocessar NFComObservação

As notas selecionadas serão reprocessadas e passarão para o status "**Não Transmitido",** caso não haja erros na validação do schema, ou **"Inconsistente"**, caso ocorra alguma falha na validação. Neste momento o  processo não faz nenhuma comunicação com a SEFAZ, apenas atualiza o XML da nota e valida seu schema, sendo necessário realizar a transmissão das notas posteriormente.

---
