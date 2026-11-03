---
content_hash: e1c7dc3edf159dabfce795d0a71160dbc1e80ae5297b9689aa2ae4453f34a8c5
fetched_at: '2026-06-29T00:10:43.670298+00:00'
page_id: '550324742'
product: rm
source: tdn-rm
title: 5.2 Zeus Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550324742
version: 13
---

Para gerar o arquivo Zeus Contábil acesse: Integração | Gerador de Saída | Layouts | Selecione o Layout Integração - Zeus Contábil, acesse Processos | Geração de Saídas

Escolha o diretório para salvar o arquivo e clique em “Avançar”

Preencha os campos da tela e clique em “Avançar” para gerar o arquivo.

* **Código da Filial:** informe o código da Filial da Coligada que está logada.
* **Data inicial e Data Final:** informe a data do lançamento contábil para seleção (data da baixa do lançamento financeiro).

As contas contábeis que não recebem CR - Centro de Responsabilidade (Centro de Custo) e UO - Unidade Organizacional (Departamento) devem ter a devida informação em seu cadastro no SGE. Para fazer este procedimento acesse **BackOffice > Gestão Contábil> Cadastros > Plano de Contas Contábil > Edite a conta contábil que NÃO deverá levar o CR e UO > vá na pasta Campos Complementares** e preencha os campos com a informação **2 - NÃO**. As contas que recebem CR e UO podem ficar com este campo em branco.

Exemplo do arquivo gerado:

1. Quando o preenchimento no campo complementar das contas contábeis for “**2 – Não**” a informação que será levada no arquivo Zeus será com o numeral nove, exemplo: 9999999999999999;
2. Quando o preenchimento no campo complementar das contas contábeis for “**1 – Sim** ou **Branco (vazio)**” a informação que será levada no arquivo Zeus serão as contas de fato.
