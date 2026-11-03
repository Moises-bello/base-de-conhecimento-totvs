---
article_id: 360024055091
category: Materiais - Compras (SIGACOM)
content_hash: 9ef0279dfcd79c945c12673253bf2bf9ae5eb1b03091673c4f2893b7b81bbd9a
fetched_at: '2026-06-28T22:41:07.568286+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o Schedule
  para Importador XML
type: support-article
updated_at: '2024-07-05T19:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024055091-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-Schedule-para-Importador-XML
---

**Dúvida**Como configurar o Schedule para Unportador xml / Totvs Colaboração

**Ambiente**Protheus – Totvs colaboração – A partir da versão 11.80  
  
**Solução**

**Schedule de Importação**  
Para o procedimento será necessário a configuração do Schedule de importação. Este Schedule será o responsável pela importação dos arquivos XML que serão recebidos via Client Neogrid no diretório “IN”, localizado dentro da instalação do Client (este é o diretório que deve ser configurado no parâmetro **MV\_NGINN**). Os arquivos serão importados para a Tabela CKO - Controle de arquivos TOTVS Colaboração. Após a gravação do arquivo na tabela, o Schedule move o arquivo da pasta IN para a pasta configurada no parâmetro **MV\_NGLIDOS**.

1. No **Configurador (SIGACFG),** acesse **Ambiente/ Schedule/ Schedule**.
2. Clique em **Agent/ Cadastro**.
3. Em **Detalhes** clique em **Incluir**.
4. Informe um nome para o agente.
5. No campo **IP** e **Porta** informe os mesmos dados do **Microsiga Protheus**.

 O ambiente é preenchido automaticamente.

1. Informe o grupo de empresas.
2. Confira dos dados e confirme.
3. Clique em **Agendamentos/Cadastro**.
4. Em **Detalhes** clique em **Incluir**.
5. Informe o nome da rotina (**colAutoRead**).
6. Selecione a empresa/ filial desejada e o módulo correspondente.
7. Clique na opção **Recorrência** e marque **Sempre Ativo**.
8. Realize o mesmo procedimento informando a rotina **SCHEDCOMCOL**
9. Clique em **Confirmar** para o agendamento.
10. Clique em **Agent** e clique em **Iniciar Todos os Serviços**.

É recomendável reiniciar o Server.

**Importante**  
No SCHEDULE da rotina COLAUTOREAD configure  apenas uma filial por Grupo de Empresas .Como a tabela CKO é única para todas empresas/ filiais e os arquivos que serão recebidos via Client também, se o Schedule for iniciado para uma empresa/ filial, processará todas as existentes.

No SCHEDULE da rotina SCHEDCOMCOL configure para todas as filiais de todos os grupos de empresa.

Caso deseje que seja apresentado no console da aplicação o procedimento que o Schedule realiza, é possível habilitar o parâmetro abaixo no arquivo appserver.ini na seção “Enviroment”:  
**COLAUTOREAD\_DEBUG=1**

**Exemplo:**

**Agent:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027011952)**

**COLAUTOREAD:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027012352)

**SCHEDCOMCOL:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027012692)

**INICIAR AGENT:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027025311)**

**INICIAR AGENDAMENTO:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027012952)**

***Saiba Mais :***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite)

[IX02 - Pontos de Entrada Importador XML](https://tdn.totvs.com/display/PROT/IX02+-+Pontos+de+Entrada)

[MP - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
