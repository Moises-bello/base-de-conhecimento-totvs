---
content_hash: 23b9d1d14b834b6773aeb201137687eb3319cb551a0d6626daca1d3fc0500152
fetched_at: '2026-06-29T00:11:53.994675+00:00'
page_id: '852913233'
product: rm
source: tdn-rm
title: Relatório do Espelho do Ponto Digital para o Totvs Assinatura Eletrônica-TAE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852913233
version: 16
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Gerar o relatório do Espelho de Ponto  enviando para o Totvs Assinatura Eletrônica -TAE |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6476](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6476) |

## **02. SITUAÇÃO/REQUISITO**

Gerar o relatório do espelho do Ponto digital para o Totvs Assinatura eletrônica -TAE.

## **03. SOLUÇÃO**

Realizar a geração do relatório do espelho do ponto digital enviando para o Totvs Assinatura Eletrônica

## **04. CONFIGURAÇÃO**

Para gerar o Espelho de Ponto enviando para o Totvs Assinatura Eletrônica é necessário realizar a instalação e configuração conforme os artigos abaixo:

1 - [Instalação Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=626926739)

2 - [Configuração do RM para integrar ao Smart View](https://tdn.totvs.com.br/pages/releaseview.action?pageId=725737666)

3 - Importar o recurso smart view **PTOTRP0002 - Espelho de Ponto Digital** através do [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento#TOTVSCompartilhamento-DownloaddeobjetogerencialnoTOTVSCompartilhamento)

## **06. EXEMPLO DE UTILIZAÇÃO**

11Gerando o Relatório Espelho de Ponto Digital para o Totvs Assinatura eletrônica2Gerando o relatório do espelho digital-Mensagens para o usuário

**Importante:**

        Mensagens de avisos serão demonstradas para o usuário caso a base não falte alguma parametrização.

* Funcionários demitidos/admitido fora do período ou funcionário que não tem batidas no período não serão considerado para a impressão. Caso exista batidas desconsideradas na AAFDT o funcionário será considerado.

Exemplo de algumas mensagens :

1-Usuário e senha não configurados ou com dados incorretos

2-Integração com o TAE  e com o Smart View sem a devida Url´s

3-Quando possui funcionários que não tem batidas no período ou não possui e-mail informado no cadastro.

3Informações Complementares

* **Parâmetros:**
  + **Imprime Nome Social:** Deve ser informado se deseja ou não exibir o nome social do funcionário. 'Verdadeiro' exibe o nome social se houver no cadastro do funcionário, 'Falso' exibe o nome civil do funcionário.
  + **Imprime  Batidas Desconsiderada:** Deve ser informado se deseja ou não exibir as marcações desconsideradas do funcionário. 'Verdadeiro' exibe as marcações desconsideradas, 'Falso' não exibe as marcações desconsideradas.

## **07. ASSUNTOS RELACIONADOS**

[Relatórios Smart View-Automação de Ponto](https://tdn.totvs.com/pages/viewpage.action?pageId=795914964)
