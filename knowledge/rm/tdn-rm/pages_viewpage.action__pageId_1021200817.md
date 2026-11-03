---
content_hash: f3bbf16982df2378ce2793fb9d563b1152df82ffe13119f4380e5cefaea3e794
fetched_at: '2026-06-29T00:05:48.018930+00:00'
page_id: '1021200817'
product: rm
source: tdn-rm
title: Central de comunicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1021200817
version: 8
---

**Caminho: Configurações > Parâmetros > RM Portal > Portal Gestão Educacional > Central de Comunicação.**

1 - Arquivo para anexos em e-mails e notificação do aplicativo

Para que seja possivel anexar arquivos no envio de mensagens do **PGE**é necessario que esse paramétro esteja configurado.

1.1 - Extensões permitidas.

Configure os tipos de arquivos permitidos separando cada extensão por ponto e vírgula ( ; ), conforme ilustrado na imagem.

1.2 – Tamanho máximo total dos anexos.

A configuração de *tamanho máximo total dos anexos* define o limite, em kilobytes (KB), que a soma de todos os arquivos anexados pode atingir.

O tamanho total combinado dos anexos não pode exceder o limite definido.

**Exemplo:** Se o limite for 10.240 KB (10 MB), é possível anexar 2 arquivos de 5 MB ou 10 arquivos de 1 MB cada.

2 - Remetente de Notificação Interna

Parâmetro para personalizar o remetente das notificações internas, que são mensagens automáticas do sistema sobre a Central de Comunicação.

3 - Habilitar o envio de e-mails por pacotes

Ativa o envio de e-mails em lotes utilizando a mesma conexão SMTP, reduzindo a sobrecarga causada pela reabertura da conexão a cada mensagem enviada.  
Essa opção pode melhorar o desempenho em ambientes com alto volume de envios.

É responsabilidade do usuário que configurar esse parâmetro avaliar, testar e validar se o envio em lote é adequado e seguro para o ambiente onde será utilizado, garantindo que o servidor SMTP suporte esse modo de operação.

3.1 - Quantidade de e-mails por pacote.

Define quantos e-mails serão enviados por pacote durante o processo.

Ajuste este parâmetro conforme a capacidade e as restrições do servidor SMTP utilizado.  
Recomendações gerais (apenas como direcionamento):  
 • Em servidores como Office 365 / Exchange Online, recomenda-se pacotes menores (20 a 50 e-mails) devido a limites de throughput e possibilidade de throttling.  
 • Servidores dedicados ou internos podem suportar pacotes maiores, mas é importante aumentar gradualmente (ex.: 50, 100, 200) e monitorar o comportamento.  
 • Para volumes elevados, utilizar pausas entre os pacotes ajuda a evitar lentidão ou bloqueios temporários.

**Observação:**  
**Os valores acima servem apenas como referência. É fundamental avaliar o servidor SMTP utilizado e realizar testes controlados para identificar a configuração**  
**mais segura e eficiente para o seu ambiente.**

3.2 - Pausar X segundos após enviar X e-mails.

Ativa uma pausa automática durante o envio de e-mails.  
A cada lote de mensagens enviados, o sistema aguardará X segundos antes de continuar, conforme configuração do usuário.

**Por que usar a pausa?**  
Ajuda a evitar throttling em servidores como Office 365 / Exchange Online, que podem limitar envios contínuos em grande volume.  
Melhora a estabilidade em processos longos, reduzindo a chance de falhas por excesso de requisições.  
Em servidores dedicados ou internos, pode não ser necessário, mas ainda pode ajudar a prevenir picos de carga.

**Dicas de uso:**  
Para Office 365: pausas de 2 a 5 segundos por lote costumam trazer maior segurança.  
Para alto volume (milhares de e-mails): considere pausas maiores ou pacotes menores.  
Ajuste gradualmente e monitore o impacto no tempo total de envio e no comportamento do servidor.

**Responsabilidade do usuário:**  
**É responsabilidade do usuário definir, testar e validar os valores de pausa e tamanho dos lotes, garantindo que atendam às limitações e**  
**capacidades do servidor SMTP utilizado.**

4 - Assistente de IA TOTVS

**IMPORTANTE:** O recurso do **Assistente de IA TOTVS na Central de Comunicação** estará disponível a partir de **19/06/2026** nas versões **12.1.2602** e **12.1.2606**.

* **Atenção:** Para a versão 12.1.2602, é obrigatória a execução do RM Atualizador.

O Assistente de IA TOTVS virá **habilitado por padrão** no RM. As permissões de acesso também serão concedidas automaticamente para todos os perfis de usuários que já possuem autorização para o envio de mensagens. Caso não deseje disponibilizar o recurso ou os acessos, será necessário desabilitá-los manualmente.

### 1. Opção "Utiliza assistente IA"

Checkbox que habilita ou desabilita globalmente as funcionalidades de inteligência artificial na Central de Comunicação .

### 2. Recursos do assistente IA de mensagem

Quando a IA está habilitada, os seguintes recursos podem ser disponibilizados para o usuário final utilizar no portal:

* **Prompt:** Permite a interação direta via comandos de texto para geração de conteúdo.
* **Revisar texto:** Aciona a correção gramatical e ortográfica automática.
* **Recriar texto:** Gera uma nova versão do texto mantendo o sentido original.
* **Tornar formal:** Ajusta o tom de voz da mensagem para uma linguagem corporativa/solene.
* **Elaborar texto:** Auxilia na criação de conteúdos do zero com base em tópicos fornecidos.

**IMPORTANTE:** O recurso do **Assistente de IA TOTVS** na Central de Comunicação estará disponível a partir da versão **12.1.2602.XXXX**, vindo **habilitado por padrão** no RM. Caso não deseje disponibilizá-lo, será necessário realizar a desativação manual nos parâmetros.

### 3. Regra de validação das mensagens

Campo destinado à inserção de **Regras de IA do usuário**.

* **Finalidade:** Definir diretrizes específicas (Ex: "Não utilizar gírias", "Sempre saudar o aluno pelo nome") que a IA deve respeitar ao processar as mensagens.

### 4. Assistente IA de Imagem (Ainda em desenvolvimento)

* **Habilitar assistente IA de Imagem:** Checkbox  para permitir a geração ou edição de imagens via IA.
* **Regra de validação das imagens:** Campo para definir restrições ou padrões visuais para as imagens geradas.

---

## Observações Importantes

**Abrangência das Configurações:** As definições realizadas nesta tela são aplicadas **automaticamente a todos os contextos**, pois a funcionalidade é compartilhada globalmente no módulo.

---

## Tabelas de Campos

| **Campo** | **Descrição** |
| --- | --- |
| **Utiliza assistente IA** | Define se o botão de IA aparecerá na interface de criação/ de mensagens. |
| **Recursos** | Determina quais recursos de ação (Revisar, Formalizar, etc.) estarão disponíveis. |
| **Regras de Validação** | Filtros e instruções customizadas para o comportamento do modelo de linguagem. |
