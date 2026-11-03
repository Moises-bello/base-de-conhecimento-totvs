---
article_id: 23970894011799
category: SIGAACD - Automação e Coleta de Dados
content_hash: f2c977e79bc22870c4c9b7826c23cf536074605ee7801d8c761761a447d84af9
fetched_at: '2026-06-28T22:39:10.982989+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configurar Local de
  impressão (ACDA060) para utilizar na impressão de Etiquetas
type: support-article
updated_at: '2026-01-27T20:17:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas
---

O artigo fornece um guia passo a passo para configurar o "Local de Impressão (ACDA060)" no sistema TOTVS Backoffice (Linha Protheus) para a impressão de etiquetas. O processo inclui a instalação e compartilhamento da impressora na rede, mapeamento da impressora via CMD para uma porta LPT e configuração dos parâmetros no sistema. Também são fornecidas instruções específicas para impressoras Zebra e links para artigos adicionais sobre automação e coleta de dados no SIGAACD.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23970919155735) Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**  
Como configurar **Local de impressão (ACDA060)** para utilizar na [impressão de Etiquetas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016771731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-ACD-para-imprimir-etiquetas?source=search)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Após realizar os cadastros na rotina **Locais de Impressão (ACDA060)** como indicado no link ([ver artigo](https://tdn.totvs.com/x/hcKfKw)), é importante revisar o passo a passo abaixo:

**1 -** Instale a impressora e seus drivers na estação de trabalho;  
**2 -** Compartilhe a impressora na rede;  
**3 -** No servidor, instale a impressora da estação que foi compartilhada na rede;  
**4 -** Mapeie, via **CMD.exe**, a impressora na porta **LPT\*** utilizando o comando: **NET USE LPT\* \\NOME\_ESTACAO\IMPRESSORA**. Esta é a porta que irá mapear: LPT1, LPT2,...

**OBS: Caso sua impressora seja Zebra e porta USB, não é necessário efetuar este passo, mas sim configurar o passo 5 conforme este TDN:** [**https://tdn.totvs.com/pages/releaseview.action?pageId=731890309**](https://tdn.totvs.com/pages/releaseview.action?pageId=731890309)

**5 -** Acesse a rotina **Locais para Impressão (ACDA060)**, e inclua um local de impressão com a seguinte configuração:

* **Código (CB5\_CODIGO)** = Informe o código desejado;
* **Descrição** = Informe a descrição desejada;
* **Modelo** = ZEBRA;
* **Porta Serial** = Nenhum;
* **Settings** = Deixe em branco;
* **Porta LPT** = Informe a porta LPT mapeada no NET USE;
* **Tipo** = Servidor;
* **Ver. Status** = Não;
* **Drv. Windows** = Não;

![ACDA060.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/23972301269399)

**6 -** Após estes passos, configure corretamente os parâmetros **MV\_IACD01, MV\_IACD02, MV\_IACD03** e **MV\_IACD04** com o **Código (CB5\_CODIGO)** das respectivas impressoras.

![MV_IACD01020304.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23972750456343)

**7 -** Teste a impressão das etiquetas.

|  |
| --- |
| **Observações:**[***Clique aqui***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016771731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-ACD-para-imprimir-etiquetas) **e veja também outras informações importantes para as configurações de impressões de Etiquetas. RDMAKES necessários, impressora Virtual, etc.** |

**NOTA:**

Para que as impressões funcionem via WEB voce precisa certificar que o uso do WEBAGENT esteja ativo em seu navegador, conforme boletim:

[Configuracao do WebAgent no browser](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent#:~:text=Ao%20habilitar%20essa%20chave%2C%20a%20op%C3%A7%C3%A3o%20%22Habilita/Desabilita%20o%20Agente%20Local%22%20n%C3%A3o%20ser%C3%A1%20mais%20exibida%20na%20tela%20de%20configura%C3%A7%C3%A3o%20para%20o%20usu%C3%A1rio.)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Como funciona a integração do ACD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016476392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-%C3%A9-configurada-a-integra%C3%A7%C3%A3o-do-SIGAACD)

[Impressão Etiquetas via Gerenciador de Impressão](https://tdn.totvs.com/x/5ugKDg)

[Procedimentos para configurar a impressora via NET USE](https://tdn.totvs.com/pages/releaseview.action?pageId=227541038)
