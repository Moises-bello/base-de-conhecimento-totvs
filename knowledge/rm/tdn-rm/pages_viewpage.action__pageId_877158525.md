---
content_hash: 2ea7d06f70b484894450846df5bb97b354ee78aec144e6d7e7c769520de8ac81
fetched_at: '2026-06-29T00:11:59.920864+00:00'
page_id: '877158525'
product: rm
source: tdn-rm
title: DT - Envio do Espelho de Ponto Digital para TOTVS Assinatura Eletrônica (TAE)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=877158525
version: 13
---

## **01. DADOS GERAIS**

| Produto: | RM |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Enviar o Espelho de Ponto Digital para o TAE |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6809](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6809), [DRHJORNRM-7163](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-7163) |

## **02. SITUAÇÃO/REQUISITO**

Criar uma tela para o envio do Espelho de Ponto Digital para Assinatura Eletrônica (TAE).

## **03. SOLUÇÃO**

Desenvolvida a tela para o envio do Espelho de Ponto Digital para Assinatura Eletrônica (TAE).

## **04. VERSÕES**

12.1.2502 e superiores

## **05. CONFIGURAÇÃO**

Para enviar o Espelho de Ponto Digital para a TOTVS Assinatura Eletrônica (TAE), é necessário realizar as seguintes configurações:

* **Recursos do Smart View**:

Certifique-se de que o recurso [PTOTRP0003 - Espelho de ponto Digital 12.1.2410 e Superiores](https://tdn.totvs.com/pages/viewpage.action?pageId=859589836) esteja importado e funcionando corretamente.

* **Autenticação no TOTVS Assinatura Eletrônica**:

Informe o usuário e a senha de autenticação em: **Configurações > Parametrizador > Iniciais > Integração > TOTVS Assinatura Eletrônica.**

* **URLs da Integração**:

Configure as URLs de integração com o TOTVS Assinatura Eletrônica em: **Ambiente > Parâmetros > Parâmetros Globais > Integração com TOTVS Assinatura Eletrônica.**

* **Permissão de Acesso**:

Permita o acesso a tela em: **Serviços Globais > Segurança > Perfis > Sistema: Automação de Ponto > Selecionar o Perfil Desejado > Editar > Acesso a Menus > 06.06 Smart View - Assinatura Eletrônica.**

## **06. EXEMPLO DE UTILIZAÇÃO**

11Sem Agendamento

1- Acessar o menu **"Relatório"** e clicar em **"Espelho Digital"**.

Importante:A partir da release 12.1.2606, a localização da funcionalidade foi alterada

Menu **"Assinatura Eletrônica" > "Envio de Relatórios" > "Espelho Digital"**

2- Preencha os parâmetros de seleção de funcionários. Os campos **"Data Início"** e **"Data Fim"** são obrigatórios. Em seguida, clique em **"Avançar"**.

3- Informe os parâmetros de impressão. O campo **"Ordenar Por"** é obrigatório. Em seguida, clique em **"Avançar"**.

4- Selecione o recurso [PTOTRP0003 - Espelho de ponto Digital 12.1.2410 e Superiores](https://tdn.totvs.com/pages/viewpage.action?pageId=859589836) e clique em **"Avançar"**. Este parâmetro também é obrigatório.

5- Após revisar as informações, clique em **"Concluir"**.

6- Para finalizar o processo, clique em **"Confirmar"**.

7- A etapa **"Conclusão do Assistente de Processo"** será exibida. Neste momento, o processo foi criado e está em execução. É possível acompanhar o andamento do processo clicando em **"Acompanhar Processo"** ou fechar a tela clicando em .

8- Caso clique em **"Acompanhar Processo"**, será exibida a tela de acompanhamento, onde poderá verificar o status do processo. Essa tela não é atualizada em tempo real; para obter atualizações do status, é necessário clicar em **"Início de Execução Recentes"**.

9- Quando o processo for concluído, isso indicará que os arquivos foram gerados. Essa informação pode ser verificada no log da tela de acompanhamento do processo ou no job executado.

* Log.

* Informação no job executado

10- Os arquivos serão enviados para a TOTVS Assinatura Eletrônica (TAE).

## **07. ASSUNTOS RELACIONADOS**
