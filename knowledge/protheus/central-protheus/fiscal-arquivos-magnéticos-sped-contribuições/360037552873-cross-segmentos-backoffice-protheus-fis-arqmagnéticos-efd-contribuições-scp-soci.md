---
article_id: 360037552873
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 41286d385d737002ec9424e208207dc689dd4f5c843fc22f95eb9f9ae08bc6e0
fetched_at: '2026-06-28T22:42:05.316661+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - SCP (Sociedade em Conta de Participação) '
type: support-article
updated_at: '2023-01-04T18:41:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037552873-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-SCP-Sociedade-em-Conta-de-Participa%C3%A7%C3%A3o
---

**Dúvida**SCP – Sociedade em Conta de Participação - EFD Contribuíções  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Sobre o SCP na EFD Contribuições, verifique a documentação abaixo:

**Caso esteja gerando somente o o arquivo magnético EFD Contribuições da empresa SCP, você precisa está logado neste Filia e empresa. Caso contrario, Seleciona Filial e selecionar a Filial SCP irá gerar o arquivo magnético correto.**

# **Observações:**

* Como a EFD Contribuições é composta por diversos fontes/programas, para saber a data de cada um deles, basta acessar a opção **"Sobre"** em **"Ações Relacionadas"**, desta forma serão exibidos os fontes e suas respectivas datas.
* A apuração e geração do arquivo EFD PIS/COFINS deverá ser efetuada através da empresa responsável (**empresa logada**) pela prestação das informações e selecionadas as filiais que irão compor as informações fiscais.

A opção que irá realizar a apuração, é a opção **“Processar Apuração da EFD Contribuições”,** ao clicar nesta opção, será necessário preencher as seguintes perguntas:

Matriz Centralizadora  
Para utilizar a rotina o sistema deverá, **obrigatoriamente**, estar logado na filial considerada **matriz**. Todo o processamento será efetuado baseando-se nesta premissa.  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=212896468>  
  
Será necessário cadastrar uma filial nova para criação de uma empresa SCP.  
  
No arquivo magnético SPED FISCAL, não existe nenhum tratamento para Sociedade Cooperativa somente no EFD Contribuições.  
  
Onde no cadastro do SIGAMAT não existe 1 campo especifico para indicar que a Filial/Empresa tal é SCP. O que vai determina sãos as regras especificas de cadas Obrigação Fiscal/Contabíl e ETC.  
  
Para parametrizar nas obrigações Contábeis etc, entrar em contato com Suporte pontual do Módulo para identificar.

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_FILSCP |
| **Tipo** | Lógico |
| **Conteúdo** | <definido pelo cliente> |
| **Descrição** | Indicação se a filial trata-se de uma SCP – Sociedade em Conta de Participação |

**Importante**  
**Parâmetro criado individualmente para cada filial. Caso seja habilitado, as informações processadas para determinada filial serão geradas com base nos procedimentos de Sociedade em Conta de Participação, conforme o Guia Prático.**  
  
**E no momento de realizar Apuração EFD Contribuições(FISA001) preencher os parâmetros de geração da seguinte maneira:**  
  
**Sociedade Cooperativa:****Informe se deverão ser processados as exclusões de base de cálculo referente Sociedade Cooperativa.**  
  
![](https://totvssuporte.zendesk.com/attachments/token/TZlWc4DUYN5G6YEw08wXUntfo/?name=inline1175567617.png)  
  
**Indicador da natureza da pessoa jurídica**  
**Selecione o Indicador da Natureza.**  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/GIupoGSq6qmpPgeVh9IKEOi8B/?name=inline1308447252.png)  
  
  
**E quando for gerar o arquivo EFD Contribuições(FISA008) preencher as perguntas para arquivo ser gerado os registros específicos de SCP:**  
  
![](https://totvssuporte.zendesk.com/attachments/token/JBRDmo7WfVivMqDjVxdJwO4Mf/?name=inline1670301871.png)
