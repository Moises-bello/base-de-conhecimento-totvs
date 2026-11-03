---
content_hash: 3879eef9ba77c77eb86ccb0c63c0e036402b17dd440a1127a03e53e5f32e60b7
fetched_at: '2026-06-29T00:05:52.641562+00:00'
page_id: '1058454855'
product: rm
source: tdn-rm
title: Portal de Imóveis - Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058454855
version: 7
---

## Este manual tem como objetivo orientar os usuários quanto à criação, edição e validação de relatórios utilizados no PI, garantindo que a impressão e a geração de PDF ocorram corretamente, sem quebras de layout.

---

### 1. Ferramenta Oficial

A ferramenta oficial utilizada pelo PI para renderização dos relatórios é o LibreOffice Writer na versão 4.2 (portable).

⚠️ **Importante:**  
Mesmo que o documento seja criado em outra ferramenta, é o LibreOffice 4.2 que será responsável pela interpretação final do arquivo e geração do PDF no sistema.

Importante!

Fontes utilizadas no Word fora do padrão Microsoft (fontes personalizadas baixadas da internet ou adquiridas pelo cliente) não são recomendadas. No entanto, o sistema possui suporte para impressão dessas fontes.

Para garantir a correta geração do PDF, é necessário seguir as orientações descritas na documentação:

---

### 2. Criação dos Relatórios

Os relatórios podem ser criados inicialmente no Microsoft Word, utilizando arquivos nos formatos:

* `.doc`
* `.docx`

Após a criação do layout, é **obrigatória** a validação no LibreOffice 4.2.

---

### 3. Validação do Layout

Todo documento deve ser validado antes do upload no sistema.

📍 Caminho da ferramenta:

*C:\Totvs\conversor-word\App\libreoffice\program***Observação:**Clientes do Cloud deverá solicitar a pasta para o cloud

▶ Abra o aplicativo ***soffice***

▶ Abra o documento criado  
▶ Verifique cuidadosamente:

* Quebras de linha e página
* Alinhamentos
* Textos sobrepostos
* Elementos fora de posição

⚠️ **Se o layout estiver quebrado no LibreOffice, o PDF gerado no PI também estará.**

---

## 4. Regras de Compatibilidade (MUITO IMPORTANTE)

O LibreOffice 4.2 possui limitações em relação ao Word. Para evitar problemas, siga rigorosamente as orientações abaixo.

---

| ⚠️ Evite usar no Word1. Shapes (Formas, linhas, círculos)  * + Exemplo: linhas, caixas, fluxogramas   + Problema: desalinham ou desaparecem no LibreOffice  ---  2. Caixas de texto (Text Box)  * + Problema: perdem posição ou sobrepõem conteúdo  ---  3. Elementos flutuantes  * + Imagens ou objetos com:     - “Quebra de texto: atrás / à frente”   + Problema: saem do lugar ou somem  ---  4. Layout com posicionamento manual (arrastar elementos)  * + Problema: não é respeitado no LibreOffice  ---  5. Fontes não padrão  * + Exemplo: Calibri, fontes personalizadas   + Problema: substituição automática → quebra de layout  ---  6. Espaçamentos manuais excessivos  * + Vários ENTER ou espaços para alinhar conteúdo   + Problema: quebra diferente no LibreOffice  ---  7. Tabelas sem estrutura definida  * + Colunas sem largura fixa   + Problema: desalinhamento automático | ✅ Boas práticas (RECOMENDADO)✔ Use tabelas para estruturar layout  * Principalmente para:   + contratos   + quadros   + layouts complexos  ---  ✔ Utilize fontes seguras  * Arial (recomendado) * Times New Roman  ---  ✔ Use alinhamento e espaçamento do próprio Word  * Evite “ajustes visuais manuais”  ---  ✔ Defina larguras fixas em tabelas  * Evita que o LibreOffice reorganize o conteúdo  ---  ✔ Use imagens “em linha com o texto”  * Nunca flutuantes  ---  ✔ Teste sempre no LibreOffice antes de subir |
| --- | --- |

---

## 5. Regra de Ouro 🚨

👉 **Se funciona no Word, mas não funciona no LibreOffice, está errado.**

👉 **O LibreOffice 4.2 é a referência final.**

---

## 6. Conclusão

Para garantir a correta impressão dos relatórios no PI:

* Crie o documento no Word (opcional)
* Sempre valide no LibreOffice 4.2
* Siga as boas práticas de compatibilidade
* Evite recursos avançados de layout
