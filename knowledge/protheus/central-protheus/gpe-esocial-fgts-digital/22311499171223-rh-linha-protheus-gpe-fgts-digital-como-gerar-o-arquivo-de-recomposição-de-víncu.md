---
article_id: 22311499171223
category: GPE - eSocial - FGTS Digital
content_hash: 6aca7e160c99d0faf2f5f76ea9c217a6aaad622588eca90158a3e80f36250a4f
fetched_at: '2026-06-28T22:44:59.330013+00:00'
product: protheus
section_id: 17829152532503
source: central-protheus
title: RH - Linha Protheus - GPE - FGTS Digital - Como gerar o Arquivo de Recomposição
  de Vínculo do FGTS
type: support-article
updated_at: '2024-09-23T19:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22311499171223-RH-Linha-Protheus-GPE-FGTS-Digital-Como-gerar-o-Arquivo-de-Recomposi%C3%A7%C3%A3o-de-V%C3%ADnculo-do-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22311499151127) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o Arquivo de Recomposição de Vínculo para envio do FGTS Digital  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210  
  
**Solução**  
Criada rotina com finalidade de geração do arquivo simplificado para recomposição do histórico do vínculo do trabalhador.  
O arquivo resultante segue o leiaute estabelecido pelo governo, conforme a versão 1.0 datada de 09/08/23, disponível para consulta no seguinte link: [Leiaute Recomposição Vínculo](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/fgts-digital-leiaute-arquivo-recomposicao-historico-do-vinculo)  
  
**Pré Requisitos:**

**1.** Ativar porta multiprotocolo ou o REST.  
Para **ativar** a **porta multiprotocolo,** acesse o appserver.ini do seu ambiente  
  
Na seção **[DRIVERS]** adicione os parâmetros:  
MULTIPROTOCOLPORT=1  
MULTIPROTOCOLPORTSECURE=0  
Exemplo:

```
[DRIVERS]  
ACTIVE=TCP  
MULTIPROTOCOLPORT=1  
MULTIPROTOCOLPORTSECURE=0
```

Na seção **[GENERAL]** adicione os parâmetros:

```
APP_ENVIRONMENT=nome_do_ambiente
```

**2.** Adicionar rotina GPEM815 no menu conforme artigo: [RH - Linha Protheus - GPE - Como excluir ou incluir rotinas no menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22311517921175)**Sugestão:** Colocar dentro do menu Miscelânea > FGTS  
  
**Navegação:**Ao acessar o novo menu criado, será aberta uma nova tela. Nessa nova tela, será exibido o menu para acesso à tela de Geração de Arquivo de Recomposição de Vínculo Empregatício.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26571537183639)**A rotina virá com a data de desligamento inicial e final automática do sistema, podendo ser alterada de acordo com a necessidade do usuário.  
  
Pode ser realizado um filtro por data de desligamento e filiais, para ser gerado em um único arquivo mais de um vinculo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26571537196951)  
  
Ou pode ser aplicado um **Filtro Avançado** que, além do período de desligamento e filial, pode ser realizado o filtro pela Matricula eSocial (Cód. Único) do funcionário tem a rescisão calculada no sistema:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26571551166743)  
  
Pode haver mais de uma filial selecionada, no entanto elas devem ter a mesma raiz de CNPJ.  
  
**Processamento:**  
Ao aplicarmos os filtros será apresentada a seguinte tela:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26571551181463)  
 **Apresentação das Informações:**Ao obter a lista de funcionários, temos as colunas:

* **CNPJ/CPF Empregador:** Correspondente a raiz do CNPJ do empregador;
* **CPF Trabalhador:** Campo RA\_CIC;
* **Dt. Admissão:** Campo RA\_ADMISSA;
* **Matrícula:** Campo RA\_CODUNIC;
* **Nome Funcionário:** Campo RA\_NOMECMP;
* **Categoria TSVE:** Campo RA\_CATEFD (mostra apenas quando a categoria é TSVE).

Além disso, temos um botão para expandir os dados de cada um dos funcionários que serão gerados no arquivo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26571537212823)  
  
**Download do Arquivo:**   
Para fazer o download do arquivo basta selecionar a opção que melhor lhe agrada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26571551195031)

**Informações:**

* O arquivo será gerado com base nas informações da tela.
* O arquivo deve conter no máximo 5.000 linhas. Caso ultrapasse esse limite, geramos mais de 1 arquivo, respeitando o limite de 5.000 linhas por arquivo.
* Esse processo também pode ser realizado diretamente na plataforma do governo. A nova rotina serve apenas para facilitar este processo.
* Documentação técnica: [DT FGTS Digital - Geração de Arquivo de Recomposição de Vínculo](https://tdn.totvs.com/pages/viewpage.action?pageId=822676259)

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - FGTS Digital - Como acessar os vídeos e perguntas frequentes disponíveis pelo governo para o FGTS Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21922796266519?source=search)  
[RH - Linha Protheus - GPE - FGTS Digital - Como será apurado no FGTS Digital os valores mensais e rescisórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21910658981399?source=search)  
[RH - Linha Protheus - GPE - FGTS Digital - Como funciona a Remuneração para fins Rescisórios no FGTS Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19454924093207?source=search)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
