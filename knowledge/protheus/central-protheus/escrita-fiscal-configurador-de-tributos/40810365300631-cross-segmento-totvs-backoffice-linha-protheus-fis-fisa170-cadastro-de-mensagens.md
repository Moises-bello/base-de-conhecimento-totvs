---
article_id: 40810365300631
category: Escrita Fiscal - Configurador de Tributos
content_hash: ce457491aeac615b8c999b74bba313c0ff646a66c74ecf0496de4232dd6c795c
fetched_at: '2026-06-28T22:39:17.280239+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Cadastro
  de Mensagens no Documento Fiscal
type: support-article
updated_at: '2026-05-28T21:32:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40810365300631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Cadastro-de-Mensagens-no-Documento-Fiscal
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40810355033751) Tempo aproximado para leitura: **10:00 min**  
  
**Dúvida**  
Como configurar mensagens fiscais no Configurador de Tributos (CFGTRIB)?  
  
**Ambiente**  
[Escreva o nome completo do Macro Segmento Produto/Área/Serviço - Produto/Área - Módulo/Serviço - mencionados acima no título e informe a Versão a qual a solução é aplicável.  
Exemplo:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da 12.1.2310  
  
**Solução**  
Módulo Livros Fiscais (SIGAFIS), no menu lateral à esquerda, clicar em Atualizações, depois em Facilitadores e logo após em Configurador de Tributos. No menu do Configurador de Tributos à esquerda acessar a pasta Mensagens:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_15-28-23.png?version=1&modificationDate=1762885703100&api=v2)

Na pasta Mensagens há 3 rotinas que serão apresentadas conforme demonstraremos o passo a passo de como utilizar a Mensageria do Configurador de Tributos.

## Cadastros e configurações

Para a demonstração utilizarei uma regra tributária previamente cadastrada.

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_15-43-12.png?version=1&modificationDate=1762886592977&api=v2)

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_15-44-31.png?version=1&modificationDate=1762886671597&api=v2)

Por ser apenas para demonstração os perfis utilizados levarão em consideração todas as possibilidades conforme a descrição dos mesmos na imagem acima.

Agora que temos o tributo, faremos o cadastro de uma mensagem:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_15-47-2.png?version=1&modificationDate=1762886822753&api=v2)

Info!

A rotina de Cadastro de Mensagem, conforme imagem acima, foi desenvolvida num momento anterior para atender Regras de Ajuste de Lançamento.  
Ela também será utilizada pela Mensageria pois nos permite criar mensagens flexíveis para serem utilizadas em obrigações acessórias como as notas fiscais e o SPED.

Após acessar a rotina de Cadastro de Mensagem e clicar em incluir teremos a seguinte tela:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_17-2-27.png?version=1&modificationDate=1762891347137&api=v2)

Info!

Para maiores informações acessar a página [CFGTRIB - Ajustes de Lançamento no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=822223872) com exemplos de utilização do cadastro de mensagem.

Acima cadastrei a seguinte mensagem "**Valor total da nota fiscal R$ [NF:TOTAL]**". Essa mensagem passara pelo processo de decodificação fazendo com o valor total da NF seja demonstrado no lugar de **NF:TOTAL**.

Agora que temos a mensagem, vamos cadastrar um identificador.

Voltando para o menu de Mensagens, temos a rotina de Identificadores ( As telas exclusivas da Mensageria serão detalhadas após essa seção Exemplo de Utilização ):

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_17-10-27.png?version=1&modificationDate=1762891828013&api=v2)

Clicando em incluir:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_17-11-51.png?version=1&modificationDate=1762891911297&api=v2)

Acima temos um exemplo de como cadastrar um identificador. Basicamente, os identificadores servirão como indicativo de onde e como devem ser gravadas as mensagens.

Atenção!

Para o devido funcionamento da rotina de cadastro de identificadores é preciso que o ambiente esteja atualizado com a patch mais recente de desenvolvimento pois os campos **Obrig.Acess**e **Finalidade**terão seus conteúdos disponibilizados pelo ambiente fiscal baseado nas atualizações do produto TSS e Fiscal Arquivos. Caso o ambiente não esteja não será possível fazer os cadastro de identificadores.

Agora que temos um identificador seguiremos para o menu das Mensagens até a rotina de Grupo de Mensagens:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_17-15-17.png?version=1&modificationDate=1762892117967&api=v2)

Ao clicar em incluir:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-17_14-51-10.png?version=1&modificationDate=1763401870970&api=v2)

Acima temos o cadastro de um grupo de mensagem. Tanto a mensagem que cadastramos quanto o identificador foram usados e há uma ênfase também no campo Tipo que define o tipo de amarração que deve ser feita para que a mensagem seja decodificada e gravada. Esses campos serão detalhados mais abaixo quando falarmos de cada tela assim como do funcionamento da rotina, mas basicamente estamos definindo todas as mensagens que fazem parte deste grupo e para cada mensagem seus possíveis destinos. Isso faz com que haja uma melhor organização no uso das mensagens. Ao agrupar as mensagens é possível designar o que irá disparar a sua decodificação através do campo Tipo, além de poder identificar cada uma delas conforme os identificadores criados.

Agora, para finalizar vamos vincular o Grupo de Mensagens na regra de cálculo que cadastramos no início pois definimos no cadastro de Grupo de Mensagens, no campo Tipo, Regra de Cálculo:

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_17-51-53.png?version=1&modificationDate=1762894313567&api=v2)

Mais abaixo, na seção Mensagens haverá o campo Cód. Grupo para que façamos a vinculação.

![](https://tdn.totvs.com/download/attachments/1013641171/image-2025-11-11_17-50-50.png?version=1&modificationDate=1762894250117&api=v2)

Documentação relacionada:

[CFGTRIB - Cadastro de Mensagens no Documento Fiscal](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Cadastro+de+Mensagens+no+Documento+Fiscal)
