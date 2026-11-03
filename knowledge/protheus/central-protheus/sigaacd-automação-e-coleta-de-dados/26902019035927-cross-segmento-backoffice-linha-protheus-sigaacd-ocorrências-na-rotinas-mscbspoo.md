---
article_id: 26902019035927
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1d23255d5fac741ca219d5fc4819a58e35a176c3b7e6bd331b976f4637acf93a
fetched_at: '2026-06-28T22:39:12.893201+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Ocorrências na rotinas
  MSCBSPOOL
type: support-article
updated_at: '2025-11-24T14:08:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26902019035927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ocorr%C3%AAncias-na-rotinas-MSCBSPOOL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26902019022871) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Ocorrências frequentes, mapeadas pelo suporte referente a rotina MSCBSPOOL. 

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Verifique na documentação a seguir a configuração e reveja todos os critérios para se certificar do correto funcionamento: [Monitor de Fila de impressão de etiquetas](https://tdn.totvs.com/pages/releaseview.action?pageId=570051440)

Após revisar a configuração, verifique cada uma das recomendações abaixo, e execute os procedimentos indicados, para sanar as principais causas de erro no monitoramento da fila de impressão.

### **Ocorrência 01:  Estou tendo dificuldades para imprimir etiquetas utilizando a rotina MSCBSPOOL.**

**Solução** - Configuração do mapeamento da impressora via NET USE revisar o boletim: [Procedimentos NET USE](https://tdn.totvs.com/pages/releaseview.action?pageId=235596006)

### **Ocorrência 02: Ao tentar imprimir uma etiqueta na rotina MSCBSPOOL, aparece a seguinte tela de erro:**

**Impressão via client exige impressora instalada na Estação.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26954131243799)

**Solução** - Caso sua impressora seja Zebra, verificar a configuração do campo CB5\_PRINTR conforme o boletim [ACDA060 - Criar campo CB5\_PRINTR](https://tdn.totvs.com/display/public/PROT/ACDA060+-+Criar+campo+CB5_PRINTR)

**Solução** - Para o correto procedimento de gerenciador de impressão via MSCBSPOOL verificar o boletim, nele temos informações sobre como configurar o local de impressão para o uso da rotina MSCBSPOOL [Gerenciador de Impressão e configuração do local de impressão(ACDA060).](https://tdn.totvs.com/pages/releaseview.action?pageId=731890309)

### **Ocorrência 03: Os parâmetros da fila de impressão da rotina MSCBSPOOL, não estão sendo salvos.**

**Solução** - A solução está documentada no link abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26902019023639)

Valide: [Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - MSCBSPOOL apagando os parâmetros. Como corrigir?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9652312385047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-MSCBSPOOL-apagando-os-par%C3%A2metros-Como-corrigir)

### **Ocorrência 04: Ao utilizar a rotina MSCBSPOOL pelo navegador, as etiquetas não estão sendo impressas.**

**Solução 04** - Para imprimir as etiquetas pelo navegador, utilizando o **WebApp** e o **WebAgent** na rotina MSCBSPOOL, siga o procedimento abaixo de configuração: [TOTVS WebAgent.](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)

**Solução** - Ao acessar a rotina MSCBSPOOL via navegador, instalar o **WebApp** e o **WebAgent** marcando a opção **"Habilitar Agente Local"** em configurações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26901986823447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26902019026711)

**Solução** - Baixe os instaladores do WebAgent a partir da [Central de Downloads.](https://suporte.totvs.com/portal/p/10098/download#company/)

### **Ocorrência 05: Ao tentar instalar o WebApp e o WebAgent, a instalação é concluída na máquina, mas ao acessar a rotina MSCBSPOOL, solicita a instalação novamente.**

**Solução** - Revisar o Certificado (SSL) do WebAgent, verificar o boletim [Certificado SSL do WebAgent](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent#id-2.WebAppWebAgent-Certificado)

### **Ocorrência 06- Ao acessar a rotina MSCBSPOOL, as etiquetas fica na fila de impressão e não são direcionadas para impressora.**

**Solução:**Validar se os parâmetros do SIGAACD estão todos configurados, com o código da impressora configurado na rotina ACDA060, verificar esse boletim aonde consta toda configuração do SIGAACD, aonde deve ser validado no seu ambiente.  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como é configurada a integração do SIGAACD?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016476392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-%C3%A9-configurada-a-integra%C3%A7%C3%A3o-do-SIGAACD)

**Solução:**Atualizar através do [Portal do Cliente](https://suporte.totvs.com/portal/p/10098/download?e=576485#all/all/all/search/TOVS%20PRINTER) o TOTVS Printer e o TOTVS Printer PDF que seria um arquivo binário utilizado como agente de impressão. Sua execução é feita por linha de comando onde os argumentos orientam a impressão.

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como atualizar o Totvs Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-atualizar-o-Totvs-Printer)

**Solução:**Através da rotina MSCBSPOOL na opção de parâmetro, configurar o **tamanho** da impressão corretamente, e deixar o campo lixeira em branco para os arquivos da pasta **Impter** localizada  **Protheus\_Data** no momento da impressão da etiqueta a mesma ser direcionada para a pasta impressos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146516701975)

### **Ocorrência 07 - Mecanismo de Hibernação das Abas do Navegador usando o MSCBSPOOL.**

Os navegadores possuem mecanismos de economia de memória que colocam as páginas que não estão em uso em hibernação, nesta situação a conexão entre o WebApp e o AppServer será interrompida.

Segue o boletim para maiores informações, avaliar o boletim no seu ambiente de homologação:

<https://tdninterno.totvs.com/display/tec/4.+Migrando+do+SmartClient+Desktop+para+o+WebApp>

### **Para mais informações sobre as recorrências mencionadas acima, segue abaixo:**

Atualização e equiparação de artefatos, manter o ambiente atualizado com todos os artefatos de atualização. Esse passo é imprescindível para o correto processamento da funcionalidade.

[- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
- [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
- [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

**Observação** : Aplicar após backups e validar primeiro em ambiente teste.

Desative as customizações, impreterivelmente conforme os três métodos recomendados na documentação: [Cross Segmentos - Linha Protheus - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus)

**Ocorrência 08:  MSCBSPOOL - Variable is not an object on IMPRIME(MSCBSPOOL.PRX) 18/07/2025 09:32**

**LINE 327**

Ao acessar a rotina MSCBSPOOL ao gerar uma etiqueta ocorre o error.log. Para solução desse caso é necessário avaliar na pasta IMPTER na Protheus\_Data os arquivos de etiquetas pendentes / corrompidos, por esse motivo apresentou o error.log.

Para solução era necessário acessar a pasta Impter na Proteus\_Data localizar a pasta da fila de impressão, exemplo Zebra / Recebimento nessa pasta apresenta todos os arquivos de impressão, e uma das etiquetas estava corrompida.

Para esse caso é necessário excluir a etiqueta que está corrompida, reiniciar o spooler de impressão do Windows do usuário em questão para solucionar o incidente.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
