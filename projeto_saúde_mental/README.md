# MentalCare - Site de Saúde Mental

Um website responsivo e moderno dedicado a saúde mental, com múltiplas páginas, carrossel de imagens interativo e design totalmente adaptável para todos os dispositivos.

## 🎨 Características Principais

### ✨ Design
- Interface moderna e amigável
- Totalmente responsivo (mobile, tablet, desktop)
- Paleta de cores profissional e acolhedora
- Animações suaves e transições elegantes

### 🖼️ Carrossel de Imagens
- Carrossel automático que avança a cada 5 segundos
- Botões de navegação (anterior/próximo)
- Indicadores de ponto para cada slide
- Navegação por teclado (setas para esquerda/direita)
- Clique nos dots para ir direto para um slide específico

### 📱 Responsividade
- Adaptado perfeitamente para dispositivos móveis (480px+)
- Layout fluido que se adapta a qualquer tamanho de tela
- Menu hamburguer em telas pequenas
- Imagens otimizadas com responsive images

### 📄 Múltiplas Páginas
1. **Home (index.html)** - Página inicial com carrossel e destaques
2. **Serviços (servicos.html)** - Descrição detalhada dos serviços
3. **Sobre (sobre.html)** - Informações sobre a empresa e equipe
4. **Recursos (recursos.html)** - Blog, artigos e guias
5. **Contato (contato.html)** - Formulário de contato e informações

## 📁 Estrutura do Projeto

```
projeto_saúde_mental/
├── index.html              # Página inicial
├── servicos.html           # Página de serviços
├── sobre.html              # Página sobre
├── recursos.html           # Página de recursos/blog
├── contato.html            # Página de contato
├── css/
│   └── style.css           # Arquivo CSS principal com responsividade
├── js/
│   └── carousel.js         # JavaScript para carrossel e interações
└── images/                 # Pasta para imagens locais (opcional)
```

## 🚀 Como Usar

### Abrir o Site
1. Navegue até a pasta `projeto_saúde_mental`
2. Abra o arquivo `index.html` em seu navegador
3. Ou clique com botão direito em `index.html` → "Abrir com" → Navegador

### Abrir em Live Server (Recomendado)
1. Abra o VSCode
2. Instale a extensão "Live Server" (by Ritwick Dey)
3. Clique com botão direito em `index.html`
4. Selecione "Open with Live Server"

## 🎯 Interações do Carrossel

### Automaticamente
- Avança para o próximo slide a cada 5 segundos

### Manualmente
- **Botões**: Clique em ❮ ou ❯ para navegar
- **Dots**: Clique em um ponto para ir direto ao slide
- **Teclado**: Use as setas esquerda/direita do teclado

## 🎨 Personalização

### Cores
Edite as cores no `css/style.css` (linhas 7-15):
```css
:root {
    --primary-color: #4CAF50;      /* Verde principal */
    --secondary-color: #2196F3;    /* Azul secundário */
    --danger-color: #f44336;       /* Vermelho */
    --text-color: #333;            /* Texto */
    --light-bg: #f5f5f5;          /* Fundo claro */
}
```

### Imagens do Carrossel
Altere as URLs de imagem no `index.html`:
```html
<img src="https://images.unsplash.com/..." alt="...">
```
Você pode usar:
- Unsplash: https://unsplash.com
- Pexels: https://pexels.com
- Pixabay: https://pixabay.com
- Ou imagens locais: `src="images/nome-imagem.jpg"`

### Texto e Conteúdo
Edite diretamente os arquivos HTML para mudar:
- Títulos
- Descrições
- Informações de contato
- Dados dos serviços
- Depoimentos

## 📱 Responsividade por Breakpoint

- **480px**: Versão mobile otimizada
- **768px**: Tablet (transição)
- **1200px**: Desktop completo

## ⌨️ Acessibilidade

- Navegação por teclado completa
- ARIA labels para leitores de tela
- Contraste de cores adequado
- Links e botões bem definidos
- Sem conteúdo apenas visual

## 🔧 Recursos Técnicos

### HTML
- Semântica correta
- Meta tags otimizadas
- Viewport configurado
- Validação HTML5

### CSS
- Grid e Flexbox
- Mobile-first approach
- Custom properties (variáveis CSS)
- Transições suaves
- Sombras e efeitos visuais

### JavaScript
- Sem dependências externas
- Vanilla JS puro
- Event listeners eficientes
- Intersection Observer para animações
- Keyboard navigation

## 📊 Seções do Site

### Home
- Carrossel de imagens
- Seção hero
- Serviços em destaque
- Testemunhos

### Serviços
- Serviços detalhados
- Planos de preços
- Fichas de comparação

### Sobre
- Quem somos
- Missão, visão e valores
- Equipe
- Estatísticas
- Certificações

### Recursos
- Blog com artigos
- Guias práticos para download
- Biblioteca de vídeos
- FAQ

### Contato
- Formulário de contato
- Informações de contato
- Mapa de localização
- Links de redes sociais
- Suporte imediato

## 💡 Dicas

1. **Performance**: As imagens são do Unsplash (otimizadas na web)
2. **SEO**: Adicione meta descriptions personalizadas em cada página
3. **Analytics**: Integre Google Analytics para rastrear visitantes
4. **Forms**: O formulário é apenas um exemplo; integre com um serviço real
5. **Certificados**: Substitua URLs de certificados fictícios pelos reais

## 🛠️ Compatibilidade

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Licença

Este projeto é livre para uso pessoal e comercial. Personalize conforme necessário!

## 📞 Suporte

Para dúvidas sobre customização, consulte:
- Documentação CSS: https://developer.mozilla.org/en-US/docs/Web/CSS
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- HTML: https://developer.mozilla.org/en-US/docs/Web/HTML

---

**Desenvolvido com ❤️ para saúde mental**
